from UI.mainUI import showMainMenu
from Helper.validation import is_valid_int
from Module.users import signup, login
from Module.Dashboard import AdminDashboard,user
from Module.students import AddStudent, ViewStudent
from Module.Attendance import Attendance, view_attendannce
from Module.Exam_Result import add_exam_result, View_Exam
from Module.fees import Fee_Record, viewfee
from Module.AddTimeTable import add_timetable, view_timetable
from Module.Notification import noticeboard, TestNotice

if __name__ == '__main__':
    option = showMainMenu()

    # MAIN LOOP
    while int(option) != 3:  
        try:
            if int(option) == 1:
                # use_role= role()
                # if use_role.lower()=="admin":
                signup()
                print("Signup Successfully")

            elif int(option) == 2 :
                 role,name,islogin= login()
                 if(role !="" and  role.lower()=="student" and islogin):
                     print(f"YOu student name {name}")


                     print("Login Successfully")

                    # DASHBOARD LOOP
                     dash_option = AdminDashboard()
                     while dash_option != 13:   # Exit dashboard when 13
                        if dash_option == 1:
                            AddStudent()
                        elif dash_option == 2:
                            ViewStudent()
                        elif dash_option == 3:
                            Attendance()
                        elif dash_option == 4:
                            view_attendannce()
                        elif dash_option == 5:
                            add_exam_result()
                        elif dash_option == 6:
                            View_Exam()
                        elif dash_option == 7:
                            Fee_Record()
                        elif dash_option == 8:
                            viewfee()
                        elif dash_option == 9:
                            add_timetable()
                        elif dash_option == 10:
                            view_timetable()
                        elif dash_option == 11:
                            noticeboard()
                        elif dash_option == 12:
                            TestNotice()
                        else:
                            print("Invalid dashboard option!")

                    # ✅ Always return to dashboard after action
                        dash_option = AdminDashboard()

            else:
                print("Invalid main menu option!")

            # ✅ Return to main menu after finishing
            option = showMainMenu()

        except ValueError:
            print("Please enter a valid number")

    print("Exiting the system... Goodbye!")