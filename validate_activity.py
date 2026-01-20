import re

activity = "LOGIN"

if re.match(r"^(LOGIN|LOGOUT|SUBMIT_ASSIGNMENT)$", activity):
    print("Valid Activity")
else:
    print("Invalid Activity")
