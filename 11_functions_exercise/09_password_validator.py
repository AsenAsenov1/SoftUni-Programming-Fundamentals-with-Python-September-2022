def validator(password1):
    pass_1 = False
    pass_2 = False
    pass_3 = False
    conditions = []
    count = 0
    if 6 <= len(password) <= 10:
        pass_1 = True
    else:
        conditions.append("Password must be between 6 and 10 characters")
    if password.isalnum():
        pass_2 = True
    else:
        conditions.append("Password must consist only of letters and digits")
    for num in password1:
        if num.isdigit():
            count += 1
            if count > 1:
                pass_3 = True
    if count < 2:
        conditions.append("Password must have at least 2 digits")
    if pass_1 == True and pass_2 == True and pass_3 == True:
        return "Password is valid"
    else:
        return "\n".join(conditions)


password = input()
print(validator(password))
