# 🔧 DevUtils Pro

**5 powerful Python CLI tools for developers — one price, forever.**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Price: $7](https://img.shields.io/badge/price-%247-orange.svg)](https://tiernocity.gumroad.com/l/pstka)

---

## 🆓 Try `organize.py` — **Free!**

This repo contains **organize.py**, a smart file organizer you can use right now:

```bash
# Download it
curl -O https://raw.githubusercontent.com/devutils-pro/devutils-pro/main/organize.py

# Analyze any messy folder (safe, no files moved)
python organize.py ~/Downloads --analyze

# Preview what will be organized
python organize.py ~/Downloads --by type

# Actually organize (after preview!)
python organize.py ~/Downloads --execute
```

**What it does:** Scans any folder, groups files by type/date/size, shows you a beautiful analysis, and optionally organizes everything into clean subfolders.

**Works on Linux, macOS, and Windows.** Python 3.8+ is all you need.

---

## 💰 Want All 5 Tools?

**organize.py** is free. The complete **DevUtils Pro** pack includes:

| # | Tool | What it does |
|---|------|-------------|
| 🗂️ | **organize** | Smart file organizer by type, date, or size |
| 📊 | **csvkit** | CSV analysis, stats, cleaning, JSON conversion |
| 🔍 | **jsonkit** | JSON pretty-print, validation, dot-notation queries |
| 📜 | **logscan** | Log file scanner with pattern detection & health stats |
| ✏️ | **renamer** | Batch file renaming with regex, numbering, case ops |

### [👉 Get the Full Pack on Gumroad — Only $7](https://tiernocity.gumroad.com/l/pstka)

One-time payment. No subscriptions. 30-day money-back guarantee.

---

## 📖 Examples

### organize (free — included in this repo)

```bash
# See what's in your Downloads
$ python organize.py ~/Downloads --analyze

📊 Directory Analysis:
   Files: 1,247
   Size:  3.2 GB

   📄 Documenti    342 files
   🖼️  Immagini     456 files
   💻 Codice        89 files
   📦 Archivi       47 files
   ...

# Organize by date (great for photos)
$ python organize.py ~/Pictures --by date --date-format "%Y/%m" --execute
✅ Done! Photos organized into year/month folders.
```

### csvkit (premium)

```bash
# Analyze any CSV in 1 second
$ python csvkit.py sales.csv --stats
📊 Rows: 15,000 | Columns: 12
   📌 revenue: Min 12.50 — Max 89,450.00 — Avg 2,341.67

# Clean + convert to JSON
$ python csvkit.py data.csv --clean clean.csv --to-json data.json
✅ Cleaned: 15,000 → 14,987 rows
✅ Converted to JSON
```

### logscan (premium)

```bash
# Health check on any log file
$ python logscan.py nginx.log
📜 File: nginx.log (1.2 GB)
   Health: 🟡 142 errors, 3,456 warnings (1.7% error rate)

# Find specific errors fast
$ python logscan.py app.log --errors --pattern "timeout"
```

### jsonkit (premium)

```bash
# Query nested JSON without installing jq
$ python jsonkit.py api.json --query "users.0.profile.email"
"john@example.com"

# See all keys in a complex JSON
$ python jsonkit.py config.json --keys
🔑 47 keys found
```

### renamer (premium)

```bash
# Preview: add prefix to 200 vacation photos
$ python renamer.py *.jpg --prefix "italy_2025_"
👁️ 200 files will be renamed

# Execute
$ python renamer.py *.jpg --prefix "italy_2025_" --execute
✅ Renamed 200/200 files
```

---

## ❓ FAQ

**Q: Why is only organize.py free?**
A: So you can see the quality before buying. If it saves you 10 minutes, you'll know the other 4 are worth it.

**Q: What do I get for $7?**
A: 5 Python scripts + README + 20 examples — full source code, no dependencies. Use them anywhere.

**Q: Can I use these at work / in CI/CD?**
A: Yes! One license = you personally. For teams of 5+ email for bulk pricing.

**Q: What if I find a bug?**
A: Open an issue on GitHub or email me — I fix bugs within 48 hours.

---

## 📦 What's in the $7 Pack

```
devutils-pro/
├── organize.py      # 🆓 FREE (this repo)
├── csvkit.py        # 💰 Premium
├── jsonkit.py       # 💰 Premium
├── logscan.py       # 💰 Premium
├── renamer.py       # 💰 Premium
├── devutils         # 💰 Premium (master command)
├── README.md        # Documentation
└── EXAMPLES.md      # 20 real-world use cases
```

---

<p align="center">
  <b>Try organize.py for free. Love it? Get all 5 for $7.</b><br>
  <a href="https://tiernocity.gumroad.com/l/pstka"><b>👉 Buy on Gumroad — $7</b></a><br><br>
  <sub>Made with ❤️ for developers who value their time.</sub>
</p>
