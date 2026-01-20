import re

log = "S101 | Asha | LOGIN | 2025-03-10 | 09:15"
pattern = r"(\d{4}-\d{2}-\d{2})\s*\|\s*(\d{2}:\d{2})"

match = re.search(pattern, log)
print("Date:", match.group(1))
print("Time:", match.group(2))
