class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.activities = []

    def add_activity(self, activity, date, time):
        self.activities.append((activity, date, time))

    def display_summary(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Activities:", self.activities)


s1 = Student("S101", "Asha")
s1.add_activity("LOGIN", "2025-03-10", "09:15")
s1.add_activity("LOGOUT", "2025-03-10", "11:30")
s1.display_summary()
