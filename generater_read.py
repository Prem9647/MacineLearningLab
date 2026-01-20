def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

for log in read_logs(r"D:\ML lab\student_activity_log\student_log.txt"):
    print(log)
