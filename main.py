def student_session():
    print("Login Success")


def log_Student():
    print(" ")
    print("Student login")
    print(" ")
    username = input(str("Enter Username: "))
    password = input(str("Enter Password: "))
    Exit = input("Exit")
    if username == "Reham":
        if password == "pass":
            student_session()
        else:
            print("invalid! Please enter user name and password again.")
    else:
        print("invalid! Please enter user name and password again.")


def admin_session():
    print("Login Success")


def log_Admin():
    print(" ")
    print("Admin login")
    print(" ")
    username = input(str("Enter Username: "))
    password = input(str("Enter Password: "))
    if username == "fatma":
        if password == "pass":
            admin_session()
        else:
            print("invalid! Please enter user name and password again.")
    else:
        print("invalid! Please enter user name and password again.")


def signup_Admin():
    print(" ")
    print("sign up")
    print(" ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    confirm_p = input("Confirm password: ")
    if password != confirm_p:
        print(" ")
        print("invalid! Please enter user name and password again.")
        print(" ")
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        confirm_p = input("Confirm password: ")
    print("Sign up successeded")


def main():
    while 1:
        print("Welcome to the Faculty System")
        print(" ")
        print("1.Admin")
        print("2.Student")
        print("3.Exit")

        user_option = input(str("Option : "))
        if user_option == "1":
            option2 = input(str("Login/signup: "))
            if option2 == "login":
                log_Admin()
            elif option2 == "signup":
                signup_Admin()
                break
        elif user_option == "2":
            log_Student()
            break
        elif user_option == "3":
            print("Exit")
            break
        else:
            print("No valid option was selected")


# main()

# pip install pandas
# pip install openpyxl
import pandas as pd
from classes import *

df = pd.read_excel('AdminData.xlsx', index_col=0)
print(df)
print("reading data done")
rows = df.iloc[0:].values
print(rows)
print(rows[0][2])
print(len(rows))

# creating admins
names = []
for name in range(len(rows)):
    names.append(rows[name][2])
print(names)
admins = []
for row in range(len(rows)):
    admin = Admin(rows[row][0], rows[row][1], rows[row][2], rows[row][3], rows[row][4], rows[row][5],
                  rows[row][6], rows[row][7], rows[row][8])
    admins.append(admin)

print("creating admins done")
print(admins[0].age)
