def check_password(password):
    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
    elif not password.isalnum():
        print("Password must consist only of letters and digits")
    elif sum(1 for c in password if c.isdigit()) < 2:
        print("Password must have at least 2 digits")
    else:
        print("Password is valid")

passw = input()
check_password(passw)
