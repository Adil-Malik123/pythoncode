import os
Students_file="AddStudent.txt"

if not os.path.exists(Students_file):
    open(Students_file, "w").close()
def AddStudent():
    name=input("Enter a name")
    Roll_No=input("Enter a Roll no")
    Select_Class=input("Enter a class")
    Email=input("Enter a Email")
    while not Email.endswith("@gmail.com"):
      Email=input("Enter a Email")
    Phone=input("Enter a Phone")
    Gender=input("Enter a Gender")
    Date_birth=input("Enter a date Birth")
    Adress=input("Enter a Adrees")
    with open(Students_file,"a") as f:
        f.write(f"{name},{Roll_No},{Select_Class},{Email},{Phone},{Gender},{Date_birth},{Adress}\n")
         
def ViewStudent():
    with open(Students_file,"r") as f:
       data= f.readlines()
    if not data:
        print("Not Data found")
        input("Press Enter to go back...")
        return  
    for line in data:
        name,roll,clas,email,phone,gender,dob,adress=line.strip().split(",")     
    print(f"Name: {name} | Roll: {roll} | Class: {clas} | Email: {email} | Phone: {phone} | Gender: {gender} | DOB: {dob} | Address: {adress}")    
    # input("\nPress Enter to return to dashboard...")   
    