import os 
from datetime import datetime
Fee_Record_File="Fee_Record.txt"
if not os.path.exists(Fee_Record_File):
     open(Fee_Record_File,"w").close()
def Fee_Record():
    Name=input("Enter a name")
    Roll_No=input("Enter a RollNO")
    month = datetime.now().month
    Fee_Status=input("Enter yes for Paid and No for Not Paid")
    while  Fee_Status not in ["yes","No"]:
         Fee_Status=input("Enter yes for Paid and No for Not Paid")
    Amount=input("Enter Amount")    
    with open(Fee_Record_File,"a") as f:
         f.write(f"{Name},{Roll_No},{month},{Fee_Status},{Amount}")
    print(" ✔Fees record saved sucessfuly")
def viewfee():
     with open(Fee_Record_File,"r") as f:
          data=f.readlines()
     if not data:
          print("invalid not found data")  
          return
     for line in data:
          name,roll,month,status,amount=line.strip().split(",")                 
          print(f" Name :{name} | Roll_No  :{roll} | Month  :{month} | Fee_Status  :{status}| Amount :{amount}")     
          input("Enter option")