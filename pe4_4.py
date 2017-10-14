def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return True
    else:
        return False


old = input()
new = input()
print(new_password(old, new))
