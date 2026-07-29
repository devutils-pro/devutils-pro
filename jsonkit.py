#!/usr/bin/env python3
"""
DevUtils Pro - JSON Toolkit
Part of the DevUtils Pro Pack

JSON pretty-printing, validation, and jq-like querying.

Usage:
  python jsonkit.py data.json                  # Pretty-print
  python jsonkit.py data.json --validate       # Validate JSON
  python jsonkit.py data.json --query "users[0].name"  # Extract value
  python jsonkit.py data.json --keys           # Show all keys
  python jsonkit.py data.json --stats          # Statistics
"""

import json
import sys
import argparse
from pathlib import Path
from collections import defaultdict

class C:
    H = '\033[95m'; B = '\033[94m'; C = '\033[96m'; G = '\033[92m'
    Y = '\033[93m'; R = '\033[91m'; BO = '\033[1m'; D = '\033[2m'; E = '\033[0m'

def c(text, color): return f"{color}{text}{C.E}"


def load_json(filepath: str):
    """Load and parse a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


def validate_json(filepath: str) -> bool:
    """Validate JSON syntax."""
    try:
        with open(filepath, 'r') as f:
            json.load(f)
        return True
    except json.JSONDecodeError as e:
        print(c(f"❌ Invalid JSON: {e}", C.R))
        return False


def query_value(data, path: str):
    """Simple dot-notation query: 'users.0.name', 'data.items.2.price'."""
    parts = path.split('.')
    current = data
    for part in parts:
        if isinstance(current, list):
            try:
                current = current[int(part)]
            except (ValueError, IndexError):
                return None
        elif isinstance(current, dict):
            current = current.get(part)
        else:
            return None
    return current


def extract_keys(data, prefix=""):
    """Recursively extract all keys from a nested JSON."""
    keys = []
    if isinstance(data, dict):
        for k, v in data.items():
            full_key = f"{prefix}.{k}" if prefix else k
            keys.append(full_key)
            keys.extend(extract_keys(v, full_key))
    elif isinstance(data, list) and data:
        keys.extend(extract_keys(data[0], f"{prefix}[*]"))
    return keys


def analyze_json(data):
    """Generate JSON statistics."""
    if isinstance(data, list):
        return {
            "type": "array",
            "length": len(data),
            "sample_keys": extract_keys(data[0])[:10] if data else []
        }
    elif isinstance(data, dict):
        return {
            "type": "object",
            "keys": list(data.keys()),
            "key_count": len(data),
            "nested_keys": extract_keys(data)[:20]
        }
    return {"type": type(data).__name__}


def main():
    parser = argparse.ArgumentParser(description="🔍 DevUtils Pro - JSON Toolkit")
    parser.add_argument("file", help="JSON file to process")
    parser.add_argument("--validate", "-v", action="store_true", help="Validate JSON syntax")
    parser.add_argument("--query", "-q", help="Query with dot notation (e.g., 'users.0.name')")
    parser.add_argument("--keys", "-k", action="store_true", help="Show all keys")
    parser.add_argument("--stats", "-s", action="store_true", help="Show statistics")
    parser.add_argument("--compact", "-c", action="store_true", help="Compact output")
    parser.add_argument("--indent", "-i", type=int, default=2, help="Indentation (default: 2)")
    
    args = parser.parse_args()
    
    print(c("\n  ╔══════════════════════════════════════╗", C.D))
    print(c("  ║     🔍 DevUtils Pro - JSONKit        ║", C.BO + C.C))
    print(c("  ╚══════════════════════════════════════╝", C.D))
    
    if not Path(args.file).exists():
        print(c(f"\n❌ File not found: {args.file}", C.R))
        sys.exit(1)
    
    # Validate
    if args.validate:
        if validate_json(args.file):
            print(c(f"\n✅ Valid JSON!", C.G))
        return
    
    data = load_json(args.file)
    file_size = Path(args.file).stat().st_size
    
    print(f"\n   File: {c(args.file, C.B)} ({c(f'{file_size/1024:.1f} KB', C.Y)})")
    
    # Stats
    if args.stats:
        analysis = analyze_json(data)
        print(c(f"\n📊 JSON Analysis:", C.BO))
        print(f"   Type:  {c(analysis['type'], C.C)}")
        if 'length' in analysis:
            print(f"   Items: {c(analysis['length'], C.Y)}")
        if 'key_count' in analysis:
            print(f"   Keys:  {c(analysis['key_count'], C.Y)}")
        if 'sample_keys' in analysis and analysis['sample_keys']:
            print(f"   Sample keys: {c(', '.join(analysis['sample_keys']), C.D)}")
        if 'nested_keys' in analysis and analysis['nested_keys']:
            print(f"   Nested keys: {c(', '.join(analysis['nested_keys'][:10]), C.D)}")
    
    # Keys
    if args.keys:
        keys = extract_keys(data)
        print(c(f"\n🔑 All Keys ({len(keys)}):", C.BO))
        for k in keys[:50]:
            print(f"   • {c(k, C.C)}")
        if len(keys) > 50:
            print(c(f"   ... and {len(keys)-50} more", C.D))
    
    # Query
    if args.query:
        result = query_value(data, args.query)
        print(c(f"\n🔎 Query: {args.query}", C.BO))
        print(json.dumps(result, indent=args.indent, ensure_ascii=False))
    
    # Pretty print (default)
    if not args.query:
        if args.compact:
            print(json.dumps(data, ensure_ascii=False, separators=(',', ':')))
        else:
            print(c(f"\n📄 Content:", C.D))
            print(json.dumps(data, indent=args.indent, ensure_ascii=False)[:5000])
            if len(json.dumps(data)) > 5000:
                print(c(f"\n... (truncated, use -c for compact)", C.D))
    
    print(c(f"\n{C.D}───", C.D))
    print(c(f"🔧 DevUtils Pro Pack — 5 powerful CLI tools for developers", C.D))
    print(c(f"   👉 https://tiernocity.gumroad.com/l/pstka — Only $7", C.BO + C.G))


if __name__ == "__main__":
    main()
