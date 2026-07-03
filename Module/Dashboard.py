def AdminDashboard():
    print("""
===============================================================
                 🌟 STUDENT MANAGEMENT SYSTEM 🌟
===============================================================

  1️⃣  Add Student
  2️⃣  View Students
  3️⃣  Attendance Record
  4️⃣  View Attendance
  5️⃣  Add Exam Result
  6️⃣  View Exam Results
  7️⃣  Add Fees Record
  8️⃣  View Fees Record
  9️⃣  Add Time Table
  🔟  View Time Table
  1️⃣1️⃣  Add Notification
  1️⃣2️⃣  Test Notification
  1️⃣3️⃣  Logout

---------------------------------------------------------------
                💡 Select an option to continue
===============================================================
""")
def user():
    print(""" ===============================================================
                 🎓 STUDENT DASHBOARD 🎓
===============================================================

  1️⃣  View Profile
  2️⃣  View Attendance
  3️⃣  View Exam Results
  4️⃣  View Fees Record
  5️⃣  View Time Table
  6️⃣  View Notifications
  7️⃣  Change Password
  8️⃣  Logout

---------------------------------------------------------------
                💡 Select an option to continue
===============================================================
""")    

    return int(input("Enter option: "))
