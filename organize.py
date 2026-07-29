#!/usr/bin/env python3
"""
DevUtils Pro - Smart File Organizer
Part of the DevUtils Pro Pack (https://[gumroad-link])

Organizes messy directories by file type, date, or size.
Runs in preview mode by default (no files moved).

Usage:
  python organize.py /path/to/messy/folder
  python organize.py /path/to/messy/folder --by date
  python organize.py /path/to/messy/folder --execute
"""

import os
import sys
import shutil
import argparse
import fnmatch
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# ─── COLOR OUTPUT ───────────────────────────────────────
class Colors:
    """Terminal colors for pretty output."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'

def color(text: str, color: str) -> str:
    return f"{color}{text}{Colors.END}"


# ─── FILE TYPE CATEGORIES ───────────────────────────────
CATEGORIES = {
    "📄 Documenti":    [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".md", ".csv", ".xls", ".xlsx", ".ppt", ".pptx"],
    "🖼️  Immagini":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico", ".tiff", ".psd", ".ai", ".eps"],
    "🎵 Audio":         [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a", ".opus"],
    "🎬 Video":         [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".3gp"],
    "💻 Codice":        [".py", ".js", ".ts", ".html", ".css", ".java", ".cpp", ".c", ".h", ".rs", ".go", ".rb", ".php", ".sql", ".sh", ".bash", ".json", ".xml", ".yaml", ".yml", ".toml", ".ini", ".env", ".gitignore", ".dockerfile"],
    "📦 Archivi":       [".zip", ".tar", ".gz", ".bz2", ".7z", ".rar", ".xz", ".tgz", ".tar.gz", ".tar.bz2", ".tar.xz"],
    "🔤 Font":          [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "⚙️  Eseguibili":    [".exe", ".msi", ".deb", ".rpm", ".app", ".bin", ".dmg", ".pkg", ".run", ".sh"],
    "📝 Altro":         []  # fallback
}


def get_category(file_path: Path) -> str:
    """Determine the category of a file based on its extension."""
    ext = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "📝 Altro"


def get_date_folder(file_path: Path, fmt: str = "%Y-%m") -> str:
    """Extract date-based folder name from file modification time."""
    mtime = os.path.getmtime(file_path)
    return datetime.fromtimestamp(mtime).strftime(fmt)


def get_size_category(file_path: Path) -> str:
    """Group files by size range."""
    size_bytes = file_path.stat().st_size
    size_mb = size_bytes / (1024 * 1024)
    
    if size_mb < 0.001:
        return "🟢 Piccolissimi (<1KB)"
    elif size_mb < 0.1:
        return "🟡 Piccoli (<100KB)"
    elif size_mb < 1:
        return "🟠 Medi (<1MB)"
    elif size_mb < 10:
        return "🔴 Grandi (<10MB)"
    else:
        return "💀 Enormi (10MB+)"


def organize_by_type(directory: Path, execute: bool = False) -> dict:
    """Organize files into subfolders by type category."""
    files_moved = {}
    
    for item in directory.iterdir():
        if not item.is_file():
            continue
        
        category = get_category(item)
        target_dir = directory / category
        
        if not execute:
            files_moved[str(item)] = str(target_dir / item.name)
        else:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_dir / item.name))
    
    return files_moved


def organize_by_date(directory: Path, execute: bool = False, fmt: str = "%Y-%m") -> dict:
    """Organize files into subfolders by modification date."""
    files_moved = {}
    
    for item in directory.iterdir():
        if not item.is_file():
            continue
        
        date_folder = get_date_folder(item, fmt)
        target_dir = directory / date_folder
        
        if not execute:
            files_moved[str(item)] = str(target_dir / item.name)
        else:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_dir / item.name))
    
    return files_moved


def organize_by_size(directory: Path, execute: bool = False) -> dict:
    """Organize files into subfolders by size range."""
    files_moved = {}
    
    for item in directory.iterdir():
        if not item.is_file():
            continue
        
        size_cat = get_size_category(item)
        target_dir = directory / size_cat
        
        if not execute:
            files_moved[str(item)] = str(target_dir / item.name)
        else:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target_dir / item.name))
    
    return files_moved


def analyze_directory(directory: Path) -> dict:
    """Analyze directory without moving any files."""
    total_files = 0
    total_size = 0
    by_category = defaultdict(lambda: {"count": 0, "size": 0})
    extensions = defaultdict(int)
    
    for item in directory.iterdir():
        if item.is_file():
            total_files += 1
            size = item.stat().st_size
            total_size += size
            
            cat = get_category(item)
            by_category[cat]["count"] += 1
            by_category[cat]["size"] += size
            
            ext = item.suffix.lower() or "(no ext)"
            extensions[ext] += 1
    
    return {
        "total_files": total_files,
        "total_size": total_size,
        "by_category": dict(by_category),
        "extensions": dict(extensions)
    }


def print_banner():
    """Print the DevUtils Pro banner."""
    print()
    print(color("  ╔══════════════════════════════════════╗", Colors.DIM))
    print(color("  ║     🛠️  DevUtils Pro - Organize      ║", Colors.BOLD + Colors.CYAN))
    print(color("  ║     Smart File Organizer v1.0        ║", Colors.DIM))
    print(color("  ╚══════════════════════════════════════╝", Colors.DIM))
    print()


def print_analysis(analysis: dict):
    """Pretty-print directory analysis."""
    total_files = analysis["total_files"]
    total_size = analysis["total_size"]
    
    print(color(f"\n📊 Directory Analysis:", Colors.BOLD))
    print(f"   Files: {color(str(total_files), Colors.YELLOW)}")
    print(f"   Size:  {color(f'{total_size / 1024:.1f} KB', Colors.YELLOW)}")
    
    if total_files == 0:
        print(f"\n   {color('✨ Directory is empty — nothing to organize!', Colors.GREEN)}")
        return
    
    print(color(f"\n   By Category:", Colors.DIM))
    for cat, info in sorted(analysis["by_category"].items(), key=lambda x: -x[1]["count"]):
        count = info["count"]
        size_kb = info["size"] / 1024
        bar_len = min(40, count * 2)
        bar = "█" * bar_len
        print(f"   {cat:20s} {color(str(count).rjust(3), Colors.YELLOW)} files  "
              f"{color(f'{size_kb:7.1f} KB', Colors.DIM)}  {color(bar, Colors.DIM)}")
    
    if analysis["extensions"]:
        print(color(f"\n   Top Extensions:", Colors.DIM))
        for ext, count in sorted(analysis["extensions"].items(), key=lambda x: -x[1])[:10]:
            print(f"   {ext:12s} {color(str(count).rjust(3), Colors.DIM)} files")


def print_preview(moves: dict, method: str):
    """Print preview of file moves."""
    if not moves:
        print(color(f"\n✅ No files to organize!", Colors.GREEN))
        return
    
    print(color(f"\n📋 Preview — Organize by {method}:", Colors.BOLD))
    print(color(f"   {len(moves)} files will be moved:", Colors.YELLOW))
    print()
    
    for i, (src, dst) in enumerate(moves.items(), 1):
        src_name = Path(src).name
        dst_dir = str(Path(dst).parent.name)
        print(f"   {color(str(i).rjust(2), Colors.DIM)}. {color(src_name, Colors.CYAN)}")
        print(f"      {color('→', Colors.DIM)} {color(dst_dir + '/', Colors.GREEN)}{src_name}")


def main():
    parser = argparse.ArgumentParser(
        description="🧹 DevUtils Pro - Smart File Organizer",
        epilog="Part of DevUtils Pro Pack — 5 powerful CLI tools for developers."
    )
    parser.add_argument("directory", nargs="?", default=".", help="Directory to organize (default: current)")
    parser.add_argument("--by", "-b", choices=["type", "date", "size"], default="type",
                        help="Organization method (default: type)")
    parser.add_argument("--execute", "-x", action="store_true", help="Actually move files (default: preview only)")
    parser.add_argument("--date-format", "-f", default="%Y-%m", help="Date format for --by date (default: %%Y-%%m)")
    parser.add_argument("--analyze", "-a", action="store_true", help="Only analyze, don't organize")
    parser.add_argument("--version", "-v", action="version", version="DevUtils Pro organize v1.0")
    
    args = parser.parse_args()
    
    print_banner()
    
    directory = Path(args.directory).resolve()
    
    if not directory.exists():
        print(color(f"\n❌ Error: Directory '{args.directory}' does not exist!", Colors.RED))
        sys.exit(1)
    
    if not directory.is_dir():
        print(color(f"\n❌ Error: '{args.directory}' is not a directory!", Colors.RED))
        sys.exit(1)
    
    print(f"   Directory: {color(str(directory), Colors.BLUE)}")
    print(f"   Method:    {color(args.by, Colors.GREEN)}")
    print(f"   Mode:      {color('PREVIEW (no changes)' if not args.execute else 'EXECUTE (will move files!)', Colors.YELLOW if not args.execute else Colors.RED)}")
    
    # Analyze
    analysis = analyze_directory(directory)
    print_analysis(analysis)
    
    if args.analyze:
        print(color("\n✅ Analysis complete.", Colors.GREEN))
        return
    
    if analysis["total_files"] == 0:
        return
    
    # Organize
    if args.by == "type":
        moves = organize_by_type(directory, execute=args.execute)
    elif args.by == "date":
        moves = organize_by_date(directory, execute=args.execute, fmt=args.date_format)
    elif args.by == "size":
        moves = organize_by_size(directory, execute=args.execute)
    else:
        moves = {}
    
    # Preview or execute
    if args.execute:
        print(color(f"\n✅ Done! {len(moves)} files organized by {args.by}.", Colors.GREEN))
        print(color(f"   Tip: Run without --execute first to preview changes.", Colors.DIM))
    else:
        print_preview(moves, args.by)
        print(color(f"\n💡 This is a PREVIEW. To execute, add --execute", Colors.YELLOW))
    
    # Upsell footer
    print(color(f"\n{Colors.DIM}───", Colors.DIM))
    print(color(f"🔧 DevUtils Pro Pack — 5 powerful CLI tools for developers", Colors.DIM))
    print(color(f"   Get all 5 tools: organize • csvkit • jsonkit • logscan • renamer", Colors.DIM))
    print(color(f"   👉 https://tiernocity.gumroad.com/l/pstka — Only $7", Colors.BOLD + Colors.GREEN))
    print()


if __name__ == "__main__":
    main()
