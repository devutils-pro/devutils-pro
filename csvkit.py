#!/usr/bin/env python3
"""
DevUtils Pro - CSV Toolkit
Part of the DevUtils Pro Pack

Powerful CSV analysis, cleaning, and conversion from the command line.

Usage:
  python csvkit.py data.csv                    # Analyze & preview
  python csvkit.py data.csv --stats            # Full statistics
  python csvkit.py data.csv --clean            # Clean bad rows
  python csvkit.py data.csv --to-json          # Convert to JSON
  python csvkit.py data.csv --filter "age>30"  # Filter rows
"""

import csv
import json
import sys
import argparse
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

# Reuse Colors from organize.py or define inline
class C:
    H = '\033[95m'; B = '\033[94m'; C = '\033[96m'; G = '\033[92m'
    Y = '\033[93m'; R = '\033[91m'; BO = '\033[1m'; D = '\033[2m'; E = '\033[0m'

def c(text, color): return f"{color}{text}{C.E}"


def load_csv(filepath: str) -> tuple:
    """Load CSV and return (headers, rows, errors)."""
    rows = []
    errors = []
    try:
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames or []
            for i, row in enumerate(reader):
                if any(v is None for v in row.values()):
                    errors.append(i + 2)
                rows.append(row)
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames or []
            for i, row in enumerate(reader):
                rows.append(row)
    return headers, rows, errors


def analyze(rows: list, headers: list) -> dict:
    """Generate comprehensive statistics."""
    stats = {
        "row_count": len(rows),
        "col_count": len(headers),
        "columns": {}
    }
    for col in headers:
        values = [r.get(col, '') for r in rows if r.get(col, '')]
        non_empty = len(values)
        nulls = len(rows) - non_empty
        
        col_stats = {
            "non_empty": non_empty,
            "nulls": nulls,
            "unique": len(set(values)),
            "top_values": Counter(values).most_common(5),
            "sample": values[:3]
        }
        
        # Try numeric stats
        nums = []
        for v in values:
            try:
                nums.append(float(v))
            except (ValueError, TypeError):
                pass
        
        if nums and len(nums) > len(values) * 0.8:
            nums.sort()
            col_stats["numeric"] = True
            col_stats['min'] = min(nums)
            col_stats['max'] = max(nums)
            col_stats['avg'] = sum(nums) / len(nums)
            col_stats['median'] = nums[len(nums) // 2]
        else:
            col_stats["numeric"] = False
        
        stats["columns"][col] = col_stats
    
    return stats


def clean_csv(filepath: str, output: str) -> tuple:
    """Remove rows with null values."""
    headers, rows, errors = load_csv(filepath)
    clean_rows = [r for r in rows if all(v is not None and v.strip() for v in r.values())]
    
    with open(output, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(clean_rows)
    
    return len(rows), len(clean_rows)


def to_json(rows: list, output: str):
    """Convert CSV rows to JSON."""
    with open(output, 'w', encoding='utf-8') as f:
        json.dump(rows, f, indent=2, ensure_ascii=False)


def filter_rows(rows: list, headers: list, condition: str) -> list:
    """Simple filter: 'col>value', 'col=value', 'col!=value'."""
    ops = {'>=': lambda a,b: float(a)>=float(b), '<=': lambda a,b: float(a)<=float(b),
           '!=': lambda a,b: a!=b, '=': lambda a,b: a==b,
           '>': lambda a,b: float(a)>float(b), '<': lambda a,b: float(a)<float(b)}
    
    for op_str, op_fn in ops.items():
        if op_str in condition:
            col, val = condition.split(op_str, 1)
            col, val = col.strip(), val.strip()
            return [r for r in rows if col in r and op_fn(r.get(col, ''), val)]
    
    print(c(f"⚠️  Unsupported filter: {condition}", C.Y))
    print(c(f"   Use: col>val | col<val | col=val | col!=val | col>=val | col<=val", C.D))
    return rows


def print_stats(stats: dict):
    """Pretty-print statistics."""
    print(c(f"\n📊 CSV Analysis:", C.BO))
    print(f"   Rows: {c(stats['row_count'], C.Y)}")
    print(f"   Columns: {c(stats['col_count'], C.Y)}")
    
    for col_name, col_stats in stats["columns"].items():
        print(c(f"\n   📌 {col_name}", C.BO))
        print(f"      Non-empty: {c(col_stats['non_empty'], C.G)}")
        if col_stats['nulls']:
            print(f"      Nulls:     {c(col_stats['nulls'], C.R)}")
        print(f"      Unique:    {c(col_stats['unique'], C.B)}")
        
        if col_stats["numeric"]:
            print(f"      Range:     {c(f'{col_stats['min']:.2f}', C.C)} — {c(f'{col_stats['max']:.2f}', C.C)}")
            print(f"      Avg:       {c(f'{col_stats['avg']:.2f}', C.C)}")
            print(f"      Median:    {c(f'{col_stats['median']:.2f}', C.C)}")
        
        if col_stats["top_values"]:
            tops = ", ".join(f"{v}({n})" for v, n in col_stats["top_values"][:3])
            print(f"      Top:       {c(tops, C.D)}")


def main():
    parser = argparse.ArgumentParser(description="📊 DevUtils Pro - CSV Toolkit")
    parser.add_argument("file", help="CSV file to process")
    parser.add_argument("--stats", "-s", action="store_true", help="Show full statistics")
    parser.add_argument("--clean", "-c", help="Clean nulls, output to FILE")
    parser.add_argument("--to-json", "-j", help="Convert to JSON, output to FILE")
    parser.add_argument("--filter", "-f", help="Filter rows (e.g., 'age>30')")
    parser.add_argument("--head", "-n", type=int, default=5, help="Show first N rows (default: 5)")
    
    args = parser.parse_args()
    
    print(c("\n  ╔══════════════════════════════════════╗", C.D))
    print(c("  ║     📊 DevUtils Pro - CSVKit         ║", C.BO + C.C))
    print(c("  ╚══════════════════════════════════════╝", C.D))
    
    if not Path(args.file).exists():
        print(c(f"\n❌ File not found: {args.file}", C.R))
        sys.exit(1)
    
    headers, rows, errors = load_csv(args.file)
    print(f"\n   File: {c(args.file, C.B)}")
    print(f"   Rows: {c(len(rows), C.Y)} | Cols: {c(len(headers), C.G)}")
    
    if errors:
        print(c(f"   ⚠️  {len(errors)} rows with null values", C.Y))
    
    # Filter if requested
    if args.filter:
        rows = filter_rows(rows, headers, args.filter)
        print(f"   After filter: {c(len(rows), C.Y)} rows")
    
    # Show head
    if rows:
        print(c(f"\n   First {min(args.head, len(rows))} rows:", C.D))
        for i, row in enumerate(rows[:args.head]):
            print(f"   {c(str(i+1).rjust(3), C.D)}. {dict(list(row.items())[:5])}")
    
    # Full stats
    if args.stats:
        stats = analyze(rows, headers)
        print_stats(stats)
    
    # Clean
    if args.clean:
        old, new = clean_csv(args.file, args.clean)
        print(c(f"\n✅ Cleaned: {old} → {new} rows ({old - new} removed)", C.G))
        print(c(f"   Saved to: {args.clean}", C.G))
    
    # To JSON
    if args.to_json:
        to_json(rows, args.to_json)
        print(c(f"\n✅ Converted {len(rows)} rows to JSON", C.G))
        print(c(f"   Saved to: {args.to_json}", C.G))
    
    # Upsell
    print(c(f"\n{C.D}───", C.D))
    print(c(f"🔧 DevUtils Pro Pack — 5 powerful CLI tools for developers", C.D))
    print(c(f"   👉 https://tiernocity.gumroad.com/l/pstka — Only $7", C.BO + C.G))


if __name__ == "__main__":
    main()
