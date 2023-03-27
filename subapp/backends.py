from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from .models import LocalAdmin, OrganisationalAdmin, SecurityPersonnel,PortalUser,StaffResident

class OrganisationalAdminBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            organisation_admin = OrganisationalAdmin.objects.get(user__email=email)
            print(organisation_admin.user.password)
            if organisation_admin and check_password(password, organisation_admin.user.password) is True:
                return organisation_admin.user.pk
        except OrganisationalAdmin.DoesNotExist:
            pass

class LocalAdminBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            local_admin = LocalAdmin.objects.get(user__email=email)
            if local_admin and check_password(password, local_admin.user.password) is True:
                return local_admin.user.pk
        except LocalAdmin.DoesNotExist:
            pass

class SecurityPersonnelBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            security_personnel=SecurityPersonnel.objects.get(user__email=email)
            if security_personnel and check_password(password, security_personnel.user.password) is True:
                return security_personnel.user.pk
        except SecurityPersonnel.DoesNotExist:
            pass


class PortalUserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            portal_user=PortalUser.objects.get(user__email=email)
            if portal_user and check_password(password, portal_user.user.password) is True:
                return portal_user.user.pk
        except PortalUser.DoesNotExist:
            pass


class StaffResidentBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            staff_resident=StaffResident.objects.get(user__email=email)
            if staff_resident and check_password(password, staff_resident.user.password) is True:
                return staff_resident.user.pk
        except StaffResident.DoesNotExist:
            pass