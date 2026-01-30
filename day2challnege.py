student_id= input("enter ur student id:")
email=input("enter ur email:")
password=input("enter ur password:")
referral=input("enter ur referral:")

valid=True

if len(student_id) != 7:
    valid = False
else:
    if student_id[0] != 'C' or student_id[1] != 'S' or student_id[2] != 'E':
        valid = False
    elif student_id[3] != '-':
        valid = False
    elif student_id[4] < '0' or student_id[4] > '9':
        valid = False
    elif student_id[5] < '0' or student_id[5] > '9':
        valid = False
    elif student_id[6] < '0' or student_id[6] > '9':
        valid = False

if valid:
    if '@' not in email or '.' not in email:
        valid = False
    elif email[0] == '@' or email[-1] == '@':
        valid = False
    elif email[-4:] != ".edu":
        valid = False

if valid:
    if len(password) < 8:
        valid = False
    elif password[0] < 'A' or password[0] > 'Z':
        valid = False
    else:
        has_digit = False
        if len(password) > 0 and password[0] >= '0' and password[0] <= '9':
            has_digit = True
        elif len(password) > 1 and password[1] >= '0' and password[1] <= '9':
            has_digit = True
        elif len(password) > 2 and password[2] >= '0' and password[2] <= '9':
            has_digit = True
        elif len(password) > 3 and password[3] >= '0' and password[3] <= '9':
            has_digit = True
        elif len(password) > 4 and password[4] >= '0' and password[4] <= '9':
            has_digit = True
        elif len(password) > 5 and password[5] >= '0' and password[5] <= '9':
            has_digit = True
        elif len(password) > 6 and password[6] >= '0' and password[6] <= '9':
            has_digit = True
        elif len(password) > 7 and password[7] >= '0' and password[7] <= '9':
            has_digit = True

        if has_digit == False:
            valid = False

if valid:
    if len(referral) != 6:
        valid = False
    elif referral[0] != 'R' or referral[1] != 'E' or referral[2] != 'F':
        valid = False
    elif referral[3] < '0' or referral[3] > '9':
        valid = False
    elif referral[4] < '0' or referral[4] > '9':
        valid = False
    elif referral[5] != '@':
        valid = False

if valid:
    print("APPROVED")
else:
    print("REJECTED")
