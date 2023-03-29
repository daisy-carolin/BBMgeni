from django.shortcuts import redirect

def check_role_is_organisational_admin(user):
    if user.is_authenticated and user.role.role_name == "OrganisationAdmin":
        return True

def check_role_is_organisationadmin_and_localadmin(user):
    if user.is_authenticated and user.role.role_name == "OrganisationAdmin" or user.is_authenticated and user.role.role_name == "LocalAdmin":
        return True
    else:
        return redirect('/login')
    
def check_role_is_localadmin_and_staffresident_and_portaluser(user):
    if user.is_authenticated and user.role.role_name == "PortalUser" or user.is_authenticated and user.role.role_name == "LocalAdmin":
        return True
    else:
        return redirect('/login')


def check_role_is_local_admin(user):
    if user.is_authenticated and user.role.role_name == "LocalAdmin":
        return True
    else:
        return redirect('/login')
    
def check_role_is_portal_user(user):
    if user.is_authenticated and user.role.role_name == "PortalUser":
        return True
    else:
        return redirect('/login')

def check_role_is_security(user):
    if user.is_authenticated and user.role.role_name == "SecurityPersonnel":
        return redirect('/checker')
    else:
        return redirect('/login')

def check_role_is_staffresident(user):
    if user.is_authenticated and user.role.role_name == "Staff/Resident":
        return True
    else:
        return redirect('/login')