# 🔧 DevUtils Pro

**5 powerful CLI tools for developers — one price, forever.**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Price: $7](https://img.shields.io/badge/price-%247-orange.svg)](https://[gumroad-link])

---

## 🎯 What is DevUtils Pro?

A curated pack of 5 professional-grade Python command-line tools that solve real problems developers face every day. No dependencies, no bloat — just copy, run, and get work done.

### The Tools

| # | Tool | What it does | Lines |
|---|------|-------------|-------|
| 🗂️ | **organize** | Smart file organizer by type, date, or size | 250 |
| 📊 | **csvkit** | CSV analysis, stats, cleaning, JSON conversion | 220 |
| 🔍 | **jsonkit** | JSON pretty-print, validation, dot-notation queries | 170 |
| 📜 | **logscan** | Log file scanner with pattern detection & stats | 210 |
| ✏️ | **renamer** | Batch file renaming with regex, numbers, case ops | 200 |

---

## ⚡ Quick Examples

### organize — Clean up messy folders

```bash
# Preview: see what will be organized
$ python organize.py ~/Downloads --analyze

📊 Directory Analysis:
   Files: 1,247
   Size:  3.2 GB

   📄 Documenti    342 files
   🖼️  Immagini     456 files
   💻 Codice        89 files
   ...

# Execute organization by type
$ python organize.py ~/Downloads --execute
✅ Done! 1,247 files organized by type.
```

### csvkit — Analyze data instantly

```bash
$ python csvkit.py sales.csv --stats

📊 CSV Analysis:
   Rows: 15,000
   Columns: 12

   📌 revenue
      Non-empty: 14,987
      Range: 12.50 — 89,450.00
      Avg: 2,341.67
      Median: 1,890.00

# Clean bad rows + convert to JSON
$ python csvkit.py sales.csv --clean sales_clean.csv --to-json sales.json
✅ Cleaned: 15,000 → 14,987 rows (13 removed)
✅ Converted 14,987 rows to JSON
```

### logscan — Find problems fast

```bash
$ python logscan.py nginx.log

   File: nginx.log (1.2 GB)
   Lines: 8,342,000
   Health: 🟡 142 errors, 3,456 warnings (1.7% error rate)

📊 Log Levels:
   INFO      7,890,000  ██████████████████████████████
   WARN          3,456  ██
   ERROR           142  █

# Drill into errors
$ python logscan.py nginx.log --errors --pattern "timeout"
```

### jsonkit — Query like jq, without installing jq

```bash
$ python jsonkit.py api-response.json --query "data.users.0.name"
"John Doe"

# Show all keys in a nested JSON (recursive)
$ python jsonkit.py config.json --keys
🔑 All Keys (47):
   • database.host
   • database.port
   • api.endpoints[*].url
   ...
```

### renamer — Rename hundreds of files in seconds

```bash
# Preview: add prefix
$ python renamer.py *.jpg --prefix "vacation_" --dir ~/photos

👁️  PREVIEW (prefix: 'vacation_'):
   47 files will be renamed:
   IMG_0001.jpg  →  vacation_IMG_0001.jpg
   IMG_0002.jpg  →  vacation_IMG_0002.jpg
   ...

# Execute + regex replace
$ python renamer.py *.txt --regex "draft_(v\d+)" --replace "final_\1" --execute
✅ Renamed 12/12 files.
```

---

## 🆚 Why DevUtils Pro?

| Feature | DevUtils Pro | Random Scripts | Online Tools |
|---------|-------------|----------------|--------------|
| Works offline | ✅ Always | ✅ | ❌ Need internet |
| Privacy | ✅ Your machine | ✅ | ❌ Data on servers |
| No dependencies | ✅ Pure Python | 🤷 | ❌ |
| Source code | ✅ Full access | ✅ | ❌ |
| AI-generated bloat | ❌ Hand-crafted | 🤷 | 🤷 |
| Works on any OS | ✅ Linux/Mac/Win | ✅ | ✅ |
| **Price** | **$7 forever** | Free (no support) | Free/$20mo |

---

## 📦 Installation

```bash
# 1. Clone or download this repo
git clone https://github.com/[username]/devutils-pro.git

# 2. Run! (no pip install needed)
cd devutils-pro
python organize.py --help
python csvkit.py --help
```

**Requirements:** Python 3.8+ (already on your machine if you're a developer)

---

## 🎁 What's included

```
devutils-pro/
├── organize.py      # Smart file organizer
├── csvkit.py        # CSV toolkit
├── jsonkit.py       # JSON toolkit
├── logscan.py       # Log scanner
├── renamer.py       # Batch file renamer
├── devutils         # Master command (run all tools)
├── README.md        # This file
└── EXAMPLES.md      # 20+ real-world examples
```

---

## 💰 Pricing

**One-time payment of $7.** No subscriptions, no hidden fees.

Includes:
- ✅ 5 CLI tools with full source code
- ✅ 20+ example use cases (EXAMPLES.md)
- ✅ Future updates (if laws/tools change)
- ✅ 30-day money-back guarantee

[👉 **Buy on Gumroad — $7**](https://[gumroad-link])

---

## 🧪 Free Sample: organize.py

Not sure? Try **organize.py** for free:

```bash
curl -O https://raw.githubusercontent.com/[username]/devutils-pro/main/organize.py
python organize.py ~/Downloads --analyze
```

If it saves you 5 minutes, imagine what all 5 tools can do.

---

## ❓ FAQ

**Q: Why Python? I use Node/Rust/Go.**
A: Python is installed on virtually every developer machine. These tools run anywhere.

**Q: Can I use these in my scripts/CI/CD?**
A: Absolutely! They return proper exit codes and work great in pipelines.

**Q: What if I find a bug?**
A: Email me ([your-email]) — I fix bugs within 48 hours. Guaranteed.

**Q: Is this really better than free alternatives?**
A: Free tools are great. These are opinionated, tested, and designed to just work™ with sensible defaults. No config files, no learning curve.

---

## 📧 Contact

- **Support:** [your-email]
- **Feature requests:** Open an issue on GitHub
- **Bulk licensing:** Email for teams of 5+

---

<p align="center">
  <b>Made with ❤️ for developers who value their time.</b><br>
  <sub>© 2025 DevUtils Pro — MIT License</sub>
</p>
