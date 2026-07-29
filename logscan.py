#!/usr/bin/env python3
"""
DevUtils Pro - Log Scanner
Part of the DevUtils Pro Pack

Scans log files for patterns, errors, timestamps and generates summaries.

Usage:
  python logscan.py server.log                     # Full analysis
  python logscan.py server.log --errors            # Only errors
  python logscan.py server.log --pattern "404"     # Search pattern
  python logscan.py server.log --time-range "10:00-12:00"  # Time filter
"""

import re
import sys
import argparse
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timedelta

class C:
    H = '\033[95m'; B = '\033[94m'; C = '\033[96m'; G = '\033[92m'
    Y = '\033[93m'; R = '\033[91m'; BO = '\033[1m'; D = '\033[2m'; E = '\033[0m'

def c(text, color): return f"{color}{text}{C.E}"

# Predefined patterns
PATTERNS = {
    "error": re.compile(r"error|fail|fatal|critical|exception", re.IGNORECASE),
    "warning": re.compile(r"warn|warning", re.IGNORECASE),
    "http_status": re.compile(r"\b(\d{3})\b"),
    "ip": re.compile(r"\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\b"),
    "timestamp": re.compile(r"\b(\d{4}[-/]\d{2}[-/]\d{2})"),
    "url": re.compile(r"\b(https?://[^\s]+)", re.IGNORECASE),
}

LOG_LEVELS = ["DEBUG", "INFO", "WARN", "WARNING", "ERROR", "FATAL", "CRITICAL", "TRACE"]

def analyze_log(filepath: str) -> dict:
    """Analyze log file and return statistics."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    
    stats = {
        "total_lines": len(lines),
        "empty_lines": sum(1 for l in lines if not l.strip()),
        "non_empty": sum(1 for l in lines if l.strip()),
    }
    
    # Count log levels
    levels = Counter()
    errors_found = []
    warnings_found = []
    ips = Counter()
    status_codes = Counter()
    
    for i, line in enumerate(lines, 1):
        for level in LOG_LEVELS:
            if re.search(rf"\b{level}\b", line):
                levels[level] += 1
                if level in ("ERROR", "FATAL", "CRITICAL"):
                    errors_found.append((i, line.strip()[:200]))
                elif level in ("WARN", "WARNING"):
                    warnings_found.append((i, line.strip()[:200]))
                break
        
        if PATTERNS["ip"].search(line):
            for ip in PATTERNS["ip"].findall(line):
                ips[ip] += 1
        
        if PATTERNS["http_status"].search(line):
            for code in PATTERNS["http_status"].findall(line):
                status_codes[code] += 1
    
    stats["levels"] = dict(levels)
    stats["errors"] = errors_found[:20]
    stats["warnings"] = warnings_found[:20]
    stats["top_ips"] = ips.most_common(10)
    stats["status_codes"] = dict(status_codes)
    stats["error_count"] = levels.get("ERROR", 0) + levels.get("FATAL", 0) + levels.get("CRITICAL", 0)
    stats["warn_count"] = levels.get("WARN", 0) + levels.get("WARNING", 0)
    
    # Calculate error rate
    if stats["non_empty"] > 0:
        stats["error_rate"] = (stats["error_count"] / stats["non_empty"]) * 100
    else:
        stats["error_rate"] = 0
    
    return stats, lines


def search_pattern(lines: list, pattern: str, context: int = 1):
    """Search for a pattern with context lines."""
    matches = []
    regex = re.compile(pattern, re.IGNORECASE)
    
    for i, line in enumerate(lines):
        if regex.search(line):
            ctx_start = max(0, i - context)
            ctx_end = min(len(lines), i + context + 1)
            context_lines = []
            for j in range(ctx_start, ctx_end):
                marker = "→" if j == i else " "
                context_lines.append(f"   {marker} {c(str(j+1).rjust(4), C.D)}: {lines[j].rstrip()[:150]}")
            matches.append("\n".join(context_lines))
    
    return matches[:30]  # Max 30 matches


def filter_by_time(lines: list, time_start: str, time_end: str):
    """Filter lines by time range (simple substring match)."""
    return [l for l in lines if time_start <= l[:len(time_start)] <= time_end]


def main():
    parser = argparse.ArgumentParser(description="📜 DevUtils Pro - Log Scanner")
    parser.add_argument("file", help="Log file to analyze")
    parser.add_argument("--errors", "-e", action="store_true", help="Show only errors")
    parser.add_argument("--warnings", "-w", action="store_true", help="Show only warnings")
    parser.add_argument("--pattern", "-p", help="Search for specific pattern (regex)")
    parser.add_argument("--context", "-c", type=int, default=1, help="Context lines for pattern search")
    parser.add_argument("--top-ips", "-i", action="store_true", help="Show top IP addresses")
    parser.add_argument("--summary", "-s", action="store_true", help="Show summary only")
    
    args = parser.parse_args()
    
    print(c("\n  ╔══════════════════════════════════════╗", C.D))
    print(c("  ║     📜 DevUtils Pro - LogScan        ║", C.BO + C.C))
    print(c("  ╚══════════════════════════════════════╝", C.D))
    
    if not Path(args.file).exists():
        print(c(f"\n❌ File not found: {args.file}", C.R))
        sys.exit(1)
    
    stats, lines = analyze_log(args.file)
    file_size = Path(args.file).stat().st_size
    
    # Summary
    print(f"\n   File: {c(args.file, C.B)} ({c(f'{file_size/1024:.1f} KB', C.Y)})")
    print(f"   Lines: {c(stats['total_lines'], C.Y)}")
    
    # Health bar
    if stats["error_count"] > 0:
        health = "🔴" if stats["error_rate"] > 5 else ("🟡" if stats["error_rate"] > 1 else "🟢")
        print(f"   Health: {health} {stats['error_count']} errors, {stats['warn_count']} warnings ({stats['error_rate']:.1f}% error rate)")
    else:
        print(f"   Health: {c('🟢 Clean!', C.G)}")
    
    # Level breakdown
    if stats["levels"]:
        print(c(f"\n📊 Log Levels:", C.BO))
        for level in LOG_LEVELS:
            if level in stats["levels"]:
                bar = "█" * min(30, stats["levels"][level])
                color = C.R if level in ("ERROR", "FATAL", "CRITICAL") else (C.Y if "WARN" in level else C.D)
                print(f"   {level:10s} {c(str(stats['levels'][level]).rjust(5), color)}  {c(bar, color)}")
    
    # Error details
    if args.errors and stats["errors"]:
        print(c(f"\n🔴 Errors:", C.R))
        for line_num, line_text in stats["errors"]:
            print(f"   {c(f'L{line_num}', C.D)}: {line_text}")
    
    if args.warnings and stats["warnings"]:
        print(c(f"\n🟡 Warnings:", C.Y))
        for line_num, line_text in stats["warnings"]:
            print(f"   {c(f'L{line_num}', C.D)}: {line_text}")
    
    # Pattern search
    if args.pattern:
        matches = search_pattern(lines, args.pattern, args.context)
        print(c(f"\n🔍 Pattern '{args.pattern}': {len(matches)} matches", C.BO))
        for m in matches[:10]:
            print(m)
        if len(matches) > 10:
            print(c(f"   ... and {len(matches)-10} more matches", C.D))
    
    # Top IPs
    if args.top_ips and stats["top_ips"]:
        print(c(f"\n🌐 Top IPs:", C.BO))
        for ip, count in stats["top_ips"]:
            print(f"   {c(ip, C.C)}: {count}")
    
    # Status codes
    if stats["status_codes"]:
        print(c(f"\n📡 HTTP Status Codes:", C.BO))
        for code, count in sorted(stats["status_codes"].items()):
            color = C.R if code.startswith('5') else (C.Y if code.startswith('4') else C.G)
            print(f"   {c(code, color)}: {count}")
    
    print(c(f"\n{C.D}───", C.D))
    print(c(f"🔧 DevUtils Pro Pack — 5 powerful CLI tools for developers", C.D))
    print(c(f"   👉 https://tiernocity.gumroad.com/l/pstka — Only $7", C.BO + C.G))


if __name__ == "__main__":
    main()
