# 📚 Examples — organize.py & DevUtils Pro

---

## 🆓 organize.py (FREE — included here)

### 1. Analyze your Downloads folder
```bash
python organize.py ~/Downloads --analyze
```
Output: file count, total size, breakdown by category, top extensions.

### 2. Preview before executing
```bash
python organize.py ~/Desktop --by type
```
Shows exactly what will move where. No changes made. Safe!

### 3. Organize by type (execute)
```bash
python organize.py ~/Downloads --by type --execute
```
📄 Documents, 🖼️ Images, 💻 Code, 📦 Archives... all sorted.

### 4. Organize photos by month
```bash
python organize.py ~/Pictures --by date --date-format "%Y/%m" --execute
```
Creates `2025/01/`, `2025/02/`, etc. subfolders.

### 5. Find disk hogs by size
```bash
python organize.py ~/Documents --by size --analyze
```
Groups files into "Small", "Medium", "Large", "Huge" — spot what to delete.

---

## 🔒 csvkit (Pro — available in full pack)

### 6. Quick stats on a CSV
```bash
python csvkit.py sales.csv --stats
```
Rows, columns, ranges, averages, null counts — in one command.

### 7. Clean CSV for database import
```bash
python csvkit.py dirty.csv --clean clean.csv
```
Removes rows with null values. Output is database-ready.

### 8. Convert CSV to JSON
```bash
python csvkit.py users.csv --to-json users.json
```
Valid JSON array, ready for any API.

### 9. Filter rows
```bash
python csvkit.py inventory.csv --filter "quantity<10"
```
Only items that need restocking.

---

## 🔒 jsonkit (Pro — available in full pack)

### 10. Pretty-print ugly JSON
```bash
python jsonkit.py minified.json
```
Readable, indented, with colors.

### 11. Validate JSON config
```bash
python jsonkit.py config.json --validate
```
Instant syntax check before deploying.

### 12. Extract nested values (like jq)
```bash
python jsonkit.py response.json --query "data.users.0.email"
```
No need to install jq. Dot-notation queries work.

---

## 🔒 logscan (Pro — available in full pack)

### 13. Health check on logs
```bash
python logscan.py /var/log/nginx/access.log
```
Error rate, status codes, top IPs — one command.

### 14. Find specific errors
```bash
python logscan.py app.log --errors --pattern "database"
```
Only database-related errors with context lines.

### 15. Top IP analysis
```bash
python logscan.py access.log --top-ips
```
Spot abuse or traffic patterns instantly.

---

## 🔒 renamer (Pro — available in full pack)

### 16. Add prefix to photos
```bash
python renamer.py *.jpg --prefix "italy_" --execute
```
IMG_0001.jpg → italy_IMG_0001.jpg

### 17. Regex replace
```bash
python renamer.py *.txt --regex "draft_(v\d+)" --replace "final_\1" --execute
```
draft_v3.txt → final_v3.txt

### 18. Sequential numbering
```bash
python renamer.py *.pdf --number "report" --padding 4 --execute
```
random.pdf → report_0001.pdf

---

## 🛒 Get the Full Pack

👉 **[Buy DevUtils Pro on Gumroad — $7](https://tiernocity.gumroad.com/l/pstka)**

All 5 tools. Full source code. One price. Forever.

---

**organize.py is free and MIT licensed. The other 4 tools are available in the Pro pack.**
