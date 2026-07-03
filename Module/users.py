import os

USERS_FILE = "users.txt"


if not os.path.exists(USERS_FILE):
    open(USERS_FILE, "w").close()
def signup():
    Name= input("Enter a name")
    email= input("Enter a email")
    while not  email.endswith("@gmail.com"):
      email= input("Enter a email")
    password= input("Enter a password")  
    while len(password)!=8:
      password= (input("Enter a password"))
    Confirm_Password= input("Enter a confirm Passsword :")  
    while Confirm_Password!=password:
          Confirm_Password= input("Enter a confirm Passsword")
    role=input("Enter Role ()")
    # --- save to file ---
    with open(USERS_FILE, "a") as f:
        f.write(f"{Name},{email},{password},{role}\n")             

def login():
    attempt=3
    while attempt>0:
        email = input("Enter email: ")
        password = input("Enter password: ")

        with open(USERS_FILE, "r") as f:
            for line in f:

                line = line.strip()
                if not line:
                    continue  

                parts = line.split(",")
                print(parts)
                if len(parts) != 4:
                    continue  

                name, stored_email, stored_password,role = parts
    
                if stored_email == email and stored_password == password:
                    print(f"Welcome {name}! Login successful")
                    print("1")
                    return  role,name,True

        attempt -= 1
        print(f"\n❌ Invalid email or password!")
        print(f"Attempts left: {attempt}\n")

        print("Invalid email or password!")
    print("2")
    return "","",False
