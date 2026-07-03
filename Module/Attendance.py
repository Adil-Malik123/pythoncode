import os
from datetime import datetime

File_Attendance="Attendance.txt"
if not os.path.exists(File_Attendance):
    open(File_Attendance,"w").close()
def Attendance():
    Name=input("Enter a name  :")
    Roll_No=input("Enter a RollNO  :")
    Select_class=input("Enter a class  :")
    date = datetime.now().strftime("%Y-%m-%d")
    Status=input("Enter P for present and A for Absent  :")
    while Status not in ["P","A"]:
        print("Invalid Input")
        Status=input("Enter P for present and A for Absent  :")
    with open("Attendance.txt","a") as f:
            f.write(f"{Name},{Roll_No},{Select_class},{Status},{date}\n")
            print("✔ Attendance saved!")

def view_attendannce():
    with open(File_Attendance, "r") as f:
        data = f.readlines()

    if not data:
        print("No attendance data found")
        return

    for line in data:
        name, roll, clas, date, status = line.strip().split(",")
        print(f"Name: {name} | Roll: {roll} | Class: {clas} | Status: {status} | Date: {date}")
