#!/usr/bin/env python3
"""
DevUtils Pro - Smart Batch Renamer
Part of the DevUtils Pro Pack

Batch rename files with regex, numbering, case conversion, and more.
Safe by default: preview mode shows changes before executing.

Usage:
  python renamer.py *.txt --regex "old_(.*)" --replace "new_\1"    # Regex
  python renamer.py *.jpg --prefix "vacation_"                      # Add prefix
  python renamer.py *.png --lowercase                                # Lowercase
  python renamer.py *.txt --number "doc"                            # Numbered sequence
  python renamer.py *.pdf --remove "draft_"                         # Remove text
"""

import os
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

class C:
    H = '\033[95m'; B = '\033[94m'; C = '\033[96m'; G = '\033[92m'
    Y = '\033[93m'; R = '\033[91m'; BO = '\033[1m'; D = '\033[2m'; E = '\033[0m'

def c(text, color): return f"{color}{text}{C.E}"


def get_files(directory: str = ".", extensions: list = None) -> list:
    """Get files in directory, optionally filtered by extension."""
    path = Path(directory)
    files = sorted([f for f in path.iterdir() if f.is_file()])
    if extensions:
        files = [f for f in files if f.suffix.lower() in [e.lower() for e in extensions]]
    return files


def plan_rename_regex(files: list, pattern: str, replace: str) -> dict:
    """Plan renames using regex find-and-replace."""
    plan = {}
    regex = re.compile(pattern)
    for f in files:
        old_name = f.name
        new_name = regex.sub(replace, old_name)
        if new_name != old_name:
            plan[f] = f.parent / new_name
    return plan


def plan_rename_prefix(files: list, prefix: str) -> dict:
    """Plan renames by adding prefix."""
    return {f: f.parent / f"{prefix}{f.name}" for f in files}


def plan_rename_suffix(files: list, suffix: str) -> dict:
    """Plan renames by adding suffix before extension."""
    plan = {}
    for f in files:
        stem = f.stem
        ext = f.suffix
        plan[f] = f.parent / f"{stem}{suffix}{ext}"
    return plan


def plan_rename_lowercase(files: list) -> dict:
    """Plan renames to lowercase."""
    return {f: f.parent / f.name.lower() for f in files if f.name != f.name.lower()}


def plan_rename_number(files: list, prefix: str, start: int = 1, padding: int = 3) -> dict:
    """Plan sequential numbering."""
    plan = {}
    for i, f in enumerate(files, start):
        num = str(i).zfill(padding)
        ext = f.suffix
        plan[f] = f.parent / f"{prefix}_{num}{ext}"
    return plan


def plan_rename_remove(files: list, text: str) -> dict:
    """Plan renames by removing text."""
    plan = {}
    for f in files:
        new_name = f.name.replace(text, "")
        if new_name != f.name:
            plan[f] = f.parent / new_name
    return plan


def plan_rename_trim(files: list, chars: int) -> dict:
    """Plan renames by trimming N characters from start."""
    plan = {}
    for f in files:
        stem = f.stem
        new_stem = stem[chars:] if chars < len(stem) else stem
        plan[f] = f.parent / f"{new_stem}{f.suffix}"
    return plan


def format_size(size_bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def main():
    parser = argparse.ArgumentParser(description="✏️  DevUtils Pro - Smart Renamer")
    parser.add_argument("files", nargs="*", default=["*"], help="Files to rename (glob supported)")
    parser.add_argument("--dir", "-d", default=".", help="Target directory (default: current)")
    parser.add_argument("--regex", "-r", help="Regex pattern to match")
    parser.add_argument("--replace", help="Replace pattern (with \\1, \\2 backreferences)")
    parser.add_argument("--prefix", help="Add prefix to all files")
    parser.add_argument("--suffix", help="Add suffix before extension")
    parser.add_argument("--lowercase", "-l", action="store_true", help="Convert to lowercase")
    parser.add_argument("--number", "-n", help="Sequential numbering with prefix (e.g., 'doc')")
    parser.add_argument("--start", type=int, default=1, help="Starting number for --number")
    parser.add_argument("--padding", type=int, default=3, help="Number padding (default: 3)")
    parser.add_argument("--remove", help="Remove this text from filenames")
    parser.add_argument("--trim", type=int, help="Trim N characters from start")
    parser.add_argument("--execute", "-x", action="store_true", help="Actually rename files!")
    parser.add_argument("--ext", help="Filter by extension (e.g., '.jpg,.png')")
    
    args = parser.parse_args()
    
    print(c("\n  ╔══════════════════════════════════════╗", C.D))
    print(c("  ║     ✏️  DevUtils Pro - Renamer        ║", C.BO + C.C))
    print(c("  ╚══════════════════════════════════════╝", C.D))
    
    directory = Path(args.dir)
    if not directory.exists():
        print(c(f"\n❌ Directory not found: {args.dir}", C.R))
        sys.exit(1)
    
    extensions = [e.strip() for e in args.ext.split(",")] if args.ext else None
    files = get_files(args.dir, extensions)
    
    if not files:
        print(c(f"\n⚠️  No files found in '{args.dir}'", C.Y))
        return
    
    print(f"\n   Directory: {c(args.dir, C.B)}")
    print(f"   Files found: {c(len(files), C.Y)}")
    
    # Build rename plan
    plan = {}
    method = ""
    
    if args.regex and args.replace:
        plan = plan_rename_regex(files, args.regex, args.replace)
        method = f"regex: '{args.regex}' → '{args.replace}'"
    elif args.prefix:
        plan = plan_rename_prefix(files, args.prefix)
        method = f"prefix: '{args.prefix}'"
    elif args.suffix:
        plan = plan_rename_suffix(files, args.suffix)
        method = f"suffix: '{args.suffix}'"
    elif args.lowercase:
        plan = plan_rename_lowercase(files)
        method = "lowercase"
    elif args.number:
        plan = plan_rename_number(files, args.number, args.start, args.padding)
        method = f"numbering: '{args.number}_###'"
    elif args.remove:
        plan = plan_rename_remove(files, args.remove)
        method = f"remove: '{args.remove}'"
    elif args.trim:
        plan = plan_rename_trim(files, args.trim)
        method = f"trim: {args.trim} chars"
    else:
        print(c(f"\n⚠️  No operation specified. Use --help for options.", C.Y))
        return
    
    if not plan:
        print(c(f"\n✅ No files need renaming!", C.G))
        return
    
    # Preview
    max_name_len = max(len(f.name) for f in plan.keys())
    
    if args.execute:
        print(c(f"\n🚀 EXECUTING rename ({method}):", C.BO + C.R))
        renamed = 0
        for old_path, new_path in plan.items():
            try:
                old_path.rename(new_path)
                renamed += 1
                print(f"   {c('✓', C.G)} {old_path.name:{max_name_len+2}s} → {c(new_path.name, C.C)}")
            except Exception as e:
                print(f"   {c('✗', C.R)} {old_path.name} — {e}")
        print(c(f"\n✅ Renamed {renamed}/{len(plan)} files.", C.G))
    else:
        print(c(f"\n👁️  PREVIEW ({method}):", C.BO))
        print(c(f"   {len(plan)} files will be renamed:", C.Y))
        print()
        for old_path, new_path in plan.items():
            old_size = format_size(old_path.stat().st_size)
            print(f"   {c(old_path.name, C.Y):{max_name_len+2}s} {c('→', C.D)} {c(new_path.name, C.C)}")
        print(c(f"\n💡 This is a PREVIEW. Add --execute to actually rename.", C.Y))
    
    print(c(f"\n{C.D}───", C.D))
    print(c(f"🔧 DevUtils Pro Pack — 5 powerful CLI tools for developers", C.D))
    print(c(f"   👉 https://tiernocity.gumroad.com/l/pstka — Only $7", C.BO + C.G))


if __name__ == "__main__":
    main()
