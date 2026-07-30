# 🗂️ organize.py — Smart File Organizer (Free)

**Clean up messy folders in 2 seconds. No dependencies. Pure Python.**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

```bash
python organize.py ~/Downloads --analyze
```

```
📊 Directory Analysis:
   Files: 1,247
   Size:  3.2 GB

   📄 Documenti    342 files  ██████████
   🖼️  Immagini     456 files  ████████████
   💻 Codice        89 files   ███
   ...
```

---

## ⚡ What it does

Scans any folder and groups files by type (documents, images, code, audio, video, archives...). Shows you exactly what's in there — sizes, counts, extensions — without moving anything.

### Features

- 🔍 **Analyze mode** — preview before making changes (default, safe)
- 📂 **Organize by type** — sort files into category folders
- 📅 **Organize by date** — group by modification date
- 📏 **Organize by size** — group by file size range
- 🎨 **Colored terminal output**
- 🐍 **Zero dependencies** — standard library only

---

## 📦 Installation

```bash
# Download the script
curl -O https://raw.githubusercontent.com/devutils-pro/devutils-pro/main/organize.py

# Run it!
python organize.py ~/Downloads --analyze
```

**Requirements:** Python 3.8+ (already on your machine)

---

## 🧪 Usage

```bash
# 1. Analyze any folder (safe, no files moved)
python organize.py ~/Downloads --analyze

# 2. Preview what would happen
python organize.py ~/Desktop --by type

# 3. Organize by type (actually moves files)
python organize.py ~/Downloads --by type --execute

# 4. Organize photos by date
python organize.py ~/Pictures --by date --date-format "%Y/%m" --execute

# 5. Group large files to find disk hogs
python organize.py ~/Documents --by size --analyze
```

---

## 🔧 Want More? Meet the Full Pack

`organize.py` is just one of **5 tools** in DevUtils Pro:

| Tool | What it does |
|------|-------------|
| 🗂️ **organize** | Smart file organizer ← *You are here (free)* |
| 📊 **csvkit** | CSV analysis, stats, clean, convert to JSON |
| 🔍 **jsonkit** | JSON pretty-print, validate, jq-like queries |
| 📜 **logscan** | Log scanner with error detection & health bar |
| ✏️ **renamer** | Batch rename with regex, numbering, prefixes |

---

## 💰 Get All 5 Tools — $7 One-Time

👉 **[Buy on Gumroad — $7](https://tiernocity.gumroad.com/l/pstka)**

- ✅ 5 CLI tools with full source code
- ✅ Works offline, zero dependencies
- ✅ Linux / macOS / Windows
- ✅ 30-day money-back guarantee
- ✅ Future updates included

---

## ❓ FAQ

**Q: Why is organize.py free?**  
A: Because it's useful on its own. Try it. If it saves you time, the full pack gives you 4 more tools for $7.

**Q: What's in the paid version?**  
A: `csvkit` (CSV superpowers), `jsonkit` (jq alternative), `logscan` (log health checks), `renamer` (batch rename magic), plus the `devutils` master command.

**Q: Can I use this at work?**  
A: Yes! One license = you personally. For teams of 5+: email for bulk pricing.

---

## 📧 Contact

- **Support:** Open an issue on GitHub
- **Bulk licensing:** Email for teams

---

<p align="center">
  <b>organize.py is free and MIT licensed.</b><br>
  <b>DevUtils Pro (full pack) is $7 on Gumroad.</b><br>
  <sub>© 2025 DevUtils Pro</sub>
</p>
