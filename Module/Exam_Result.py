import os
Exam_Result_File="Exam_Result.txt"

if not os.path.exists(Exam_Result_File):
    open(Exam_Result_File,"w").close()
def add_exam_result():
    Subject=input("Enter a Subject ")
    Obtained_Mark=input("Enter Obtained Mark")
    Grade=input("Enter Grade")
    Total_Mark=input("Enter total Mark")
    with open(Exam_Result_File,"a") as f:
        f.write(f"{Subject},{Obtained_Mark},{Grade},{Total_Mark}\n")
    print("✔ Exam result saved successfully!") 


def View_Exam():
    with open(Exam_Result_File,"r") as f:
        data=f.readlines()
    if not data:
        print("Invalid Data not Found")    
    for line in data:
        subject,ob_marks,grade,T_marks=line.strip().split(",")    
    print(f"Subject :{subject}| Obtained_Marks :{ob_marks} |Grade :{grade} | TOtal_Marks :{T_marks}")    
    