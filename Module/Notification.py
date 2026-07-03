import os
from datetime import datetime 
Notice_Board_File="Notification.txt"
if not os.path.exists(Notice_Board_File):
    open(Notice_Board_File, "w").close()
def noticeboard():
    Notice=input("Add a notice ")
    date = datetime.now().strftime("%Y-%m-%d")
    Section=input("Enter a section :")
    with open(Notice_Board_File,"a") as f:
        f.write(f"Notice :{Notice} | Date  :{date} | Section :{Section}\n")
    
    print("\n✔ Notification added successfully!\n")


Test_Notice_File="Notification.txt"
if not os.path.exists(Test_Notice_File):
    open(Test_Notice_File, "w").close()
def TestNotice():
    Subject=input("Enter a Subject")    
    date = datetime.now().strftime("%Y-%m-%d")
    with open(Notice_Board_File,"a") as f:
        f.write(f"Subject :{Subject} | Date  :{date} |" )
    
    print("\n✔ Test Notification added successfully!\n")    