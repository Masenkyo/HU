def new_password(oldpassword, newpassword):
    return newpassword != oldpassword and len(newpassword) >= 6 and any(char.isdigit() for char in newpassword)
print(f'your new password is {new_password(input('enter old password: '), input('enter new password: '))}')