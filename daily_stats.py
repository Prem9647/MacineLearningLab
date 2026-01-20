logs = [
    ("LOGIN", "2025-03-10"),
    ("LOGOUT", "2025-03-10"),
    ("LOGIN", "2025-03-11")
]

stats = {}

for act, date in logs:
    stats[(date, act)] = stats.get((date, act), 0) + 1

for key, value in stats.items():
    print(key, ":", value)
