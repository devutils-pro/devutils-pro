# 📚 EXAMPLES.md — 20 Real-World Use Cases

---

## 🗂️ organize — Smart File Organizer

### 1. Clean your Downloads folder
```bash
python organize.py ~/Downloads --by type --execute
# Result: 1,247 files sorted into Documents, Images, Code, Archives...
```

### 2. Organize by date (great for photos)
```bash
python organize.py ~/Pictures --by date --date-format "%Y/%m" --execute
# Result: /Pictures/2025/01/, /Pictures/2025/02/, ...
```

### 3. Group large files for cleanup
```bash
python organize.py ~/Desktop --by size --analyze
# Result: See which files are 10MB+, decide what to delete
```

### 4. Preview before executing (always!)
```bash
python organize.py ~/Documents --by type
# Result: Shows exactly what will move where, no changes made
```

---

## 📊 csvkit — CSV Toolkit

### 5. Quick stats on a large dataset
```bash
python csvkit.py sales_2025.csv --stats
# Result: Row count, column ranges, averages, null counts in 2 seconds
```

### 6. Clean CSV for import into database
```bash
python csvkit.py dirty_data.csv --clean clean_data.csv
# Result: All rows with nulls removed, ready for PostgreSQL
```

### 7. Convert CSV to JSON for API
```bash
python csvkit.py users.csv --to-json users.json
# Result: Valid JSON array ready to send to an API
```

### 8. Filter rows by condition
```bash
python csvkit.py inventory.csv --filter "quantity<10"
# Result: Only items that need restocking
```

---

## 🔍 jsonkit — JSON Toolkit

### 9. Pretty-print ugly minified JSON
```bash
python jsonkit.py api-response.json
# Result: Beautifully formatted JSON you can actually read
```

### 10. Validate JSON before deploying config
```bash
python jsonkit.py config.json --validate
# Result: ✅ Valid JSON! or ❌ Invalid JSON: line 42, missing comma
```

### 11. Extract nested values without jq
```bash
python jsonkit.py response.json --query "data.users.0.profile.email"
# Result: "john@example.com"
```

### 12. Explore unknown JSON structure
```bash
python jsonkit.py mystery.json --keys
# Result: All 47 nested keys listed, know what you're working with
```

---

## 📜 logscan — Log Scanner

### 13. Health check on production logs
```bash
python logscan.py /var/log/nginx/access.log
# Result: Error rate, top IPs, status code breakdown in 1 command
```

### 14. Find specific errors fast
```bash
python logscan.py app.log --errors --pattern "database"
# Result: Only database-related errors with context
```

### 15. Analyze who's hitting your server
```bash
python logscan.py access.log --top-ips
# Result: Top 10 IPs by request count → spot abuse
```

### 16. Check HTTP status distribution
```bash
python logscan.py access.log --summary
# Result: Green 200s, yellow 404s, red 500s — instant overview
```

---

## ✏️ renamer — Batch File Renamer

### 17. Add prefix to vacation photos
```bash
python renamer.py *.jpg --prefix "italy_2025_" --execute
# Result: IMG_0001.jpg → italy_2025_IMG_0001.jpg
```

### 18. Rename draft files to final versions
```bash
python renamer.py *.txt --regex "draft_(v\d+)" --replace "final_\1" --execute
# Result: draft_v3.txt → final_v3.txt
```

### 19. Number exported files sequentially
```bash
python renamer.py *.pdf --number "report" --padding 4 --execute
# Result: random.pdf → report_0001.pdf, another.pdf → report_0002.pdf
```

### 20. Strip annoying prefixes from downloads
```bash
python renamer.py *.mp4 --remove "downloaded_from_site_" --execute
# Result: downloaded_from_site_video.mp4 → video.mp4
```

---

**All examples tested on Python 3.8+, Linux/Mac/Windows.**
