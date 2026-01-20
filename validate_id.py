import re

student_id = "S101"

if re.match(r"^S\d+$", student_id):
    print("Valid Student ID")
else:
    print("Invalid Student ID")
