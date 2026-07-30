# 📚 EXAMPLES.md — Real-World Use Cases

## 🗂️ organize (free — in this repo)

### 1. Analyze your Downloads folder
```bash
python organize.py ~/Downloads --analyze
```
Shows: 1,247 files, 3.2 GB, grouped by type with sizes.

### 2. Organize by file type
```bash
python organize.py ~/Desktop --by type --execute
```
Result: Files sorted into Documents, Images, Code, Archives, Audio...

### 3. Organize photos by date
```bash
python organize.py ~/Pictures --by date --date-format "%Y/%m" --execute
```
Result: `/Pictures/2025/01/`, `/Pictures/2025/02/`, etc.

### 4. Find large files to delete
```bash
python organize.py ~/Desktop --by size --analyze
```
See which files are 10MB+ before deciding to delete them.

---

## 📊 csvkit (premium — in the $7 pack)

### 5. Quick stats on a large CSV
```bash
python csvkit.py sales_2025.csv --stats
```

### 6. Clean CSV for database import
```bash
python csvkit.py dirty_data.csv --clean clean_data.csv
```

### 7. Convert CSV to JSON
```bash
python csvkit.py users.csv --to-json users.json
```

### 8. Filter rows by condition
```bash
python csvkit.py inventory.csv --filter "quantity<10"
```

---

## 🔍 jsonkit (premium — in the $7 pack)

### 9. Pretty-print any JSON
```bash
python jsonkit.py api-response.json
```

### 10. Validate JSON before deploy
```bash
python jsonkit.py config.json --validate
```

---

## 📜 logscan (premium — in the $7 pack)

### 11. Health check on production logs
```bash
python logscan.py /var/log/nginx/access.log
```

### 12. Find specific errors
```bash
python logscan.py app.log --errors --pattern "database"
```

---

## ✏️ renamer (premium — in the $7 pack)

### 13. Batch rename vacation photos
```bash
python renamer.py *.jpg --prefix "italy_2025_" --execute
```

### 14. Rename with regex
```bash
python renamer.py *.txt --regex "draft_(v\d+)" --replace "final_\1" --execute
```

---

**Want all tools? [Get the pack on Gumroad — $7](https://tiernocity.gumroad.com/l/pstka)**
