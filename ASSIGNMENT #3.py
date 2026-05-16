username = "Mahmoud"
password = "00000000$*"
role = "admin"

entered_username = input("Enter your username: ")
if entered_username == username:
    entered_password = input("Enter the password: ")
    if entered_password == password:
        if role == "admin":
            print("Welcome Admin")
        elif role == "moderator":
            print("Welcome Moderator")
        elif role == "user":
            print("Welcome User")
        else:
            print("Unknown role") 
    else:
        print("Wrong Password")
else: 
    print("User not found")
