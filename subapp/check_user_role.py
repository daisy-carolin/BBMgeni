def check_role_is_organisational_admin(user):
    print(user)
    if user.is_authenticated and user.role == "Local Admin":
        return True
