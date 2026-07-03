import os

TIMETABLE_FILE = "TimeTable.txt"

if not os.path.exists(TIMETABLE_FILE):
    open(TIMETABLE_FILE, "w").close()

def add_timetable():
    print("\n===== ADD TIME TABLE =====")

    Class = input("Enter Class (e.g., 10th, 9th,  1st Semester): ")
    Day = input("Enter Day (Monday–Sunday): ")
    Subject = input("Enter Subject Name: ")
    Start_Time = input("Enter Start Time (e.g., 9:00 AM): ")
    End_Time = input("Enter End Time (e.g., 10:00 AM): ")
    Teacher = input("Enter Teacher Name: ")

    # Save data into file
    with open(TIMETABLE_FILE, "a") as f:
        f.write(f"{Class},{Day},{Subject},{Start_Time},{End_Time},{Teacher}\n")

    print("\n✔ Time table record added successfully!\n")


def view_timetable():
    print("\n===== VIEW TIME TABLE =====")
    with open(TIMETABLE_FILE, "r") as f:
        data = f.readlines()

    if not data:
        print("No timetable records found.")
        return

    for line in data:
        Class, Day, Subject, Start_Time, End_Time, Teacher = line.strip().split(",")

        print(f"""
  Class: {Class} | Day: {Day}| Subject: {Subject} |Time: {Start_Time} - {End_Time}| Teacher: {Teacher}
---------------------------------------------
        """)
