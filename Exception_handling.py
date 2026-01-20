log = "INVALID LOG ENTRY"

try:
    parts = log.split("|")
    if len(parts) != 5:
        raise ValueError("Invalid log format")
except Exception as e:
    print("Error:", e)
