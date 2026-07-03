import os

Teacher_Record_File="Teacher_Record.txt"
if not os.path.exists(Teacher_Record_File):
     open(Teacher_Record_File,"w").close()
def Teacher_Record():
        Name=input("Enter a name")
        Qualification=input("Enter a Qualification ")
        Subject=input("Enter a Subject ")
        Telephone=input("Enter a Telephone No ")
        email= input("Enter a email")
        while not  email.endswith("@gmail.com"):
          email= input("Enter a email")
        with open(Teacher_Record_File,"a") as f:
             f.write(f"{Name},{Qualification},{Subject},{Telephone},{email}")  
        print("✔  Teacher Record Saved Sucessfuly")     
def viewTeacher():
     with open(Teacher_Record_File,"r") as f:
          data=f.readlines()
     if not data:
          print("Data not found") 
          return    
     for line in data:
          name,qualification,subject,tel,email=line.strip().split(",")     
     print(f"Name :{name}| Qualification :{qualification} | Subject :{subject} | Phone No :{tel} | Email :{email}")     