activities = ["LOGIN", "LOGIN", "SUBMIT_ASSIGNMENT"]

login_count = 0
for act in activities:
    if act == "LOGIN":
        login_count += 1
    elif act == "LOGOUT":
        login_count -= 1

if login_count > 0:
    print("Abnormal behavior: Login without Logout")
