file = open(r"D:\ML lab\student_activity_log\student_log.txt", "r")
for line in file:
    print(line.strip())
file.close()
