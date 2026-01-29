fullname = input("enter your full name:")
email = input("enter your email id: ")
mobile = input("enter mobile number: ")
age = int(input("enter age: "))

valid = True

if fullname[0] == " " or fullname[-1] == " ":
    valid = False

if fullname.count(" ") < 1:
    valid = False

if email.count("@") != 1:
    valid = False

if email.count(".") < 1:
    valid = False

if email[0] == "@":
    valid = False

if len(mobile) != 10:
    valid = False

if mobile[0] == "0":
    valid = False

if mobile.isdigit() == False:
    valid = False

if age < 18 or age > 60:
    valid = False

if valid:
    print("user profile is valid")
else:
    print("user profile is invalid")
