def check_role_is_organisational_admin(user):
    print(user)
    if user.is_authenticated and user.is_organisationadmin:
        return True

def check_role_is_organisationadmin_and_localadmin(user):
    if user.is_authenticated and user.is_localadmin or user.is_authenticated and user.is_organisationadmin:
        return True
    
def check_role_is_localadmin_and_staffresident_and_portaluser(user):
    if user.is_authenticated and user.is_localadmin or user.is_authenticated and user.is_organisationadmin:
        return True


def check_role_is_local_admin(user):
    if user.is_authenticated and user.is_localadmin:
        return True
    
def check_role_is_portal_user(user):
    if user.is_authenticated and user.is_portaluser:
        return True

def check_role_is_security(user):
    if user.is_authenticated and user.is_securitypersonel:
        return True

def check_role_is_staffresident(user):
    if user.is_authenticated and user.is_staffresident:
        return True