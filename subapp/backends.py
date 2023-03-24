from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from .models import LocalAdmin, OrganisationalAdmin, SecurityPersonnel,PortalUser,StaffResident

class OrganisationalAdminBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            organisation_admin = OrganisationalAdmin.objects.get(email=email)
            if organisation_admin and check_password(password, organisation_admin.password) is True:
                return organisation_admin.email
        except OrganisationalAdmin.DoesNotExist:
            pass

class LocalAdminBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            local_admin = LocalAdmin.objects.get(email=email)
            if local_admin and check_password(password, local_admin.password) is True:
                return local_admin.email
        except LocalAdmin.DoesNotExist:
            pass

class SecurityPersonnelBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            security_personnel=SecurityPersonnel.objects.get(email=email)
            if security_personnel and check_password(password, security_personnel.password) is True:
                return security_personnel.email
        except SecurityPersonnel.DoesNotExist:
            pass


class PortalUserBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            portal_user=PortalUser.objects.get(email=email)
            if portal_user and check_password(password, portal_user.password) is True:
                return portal_user.email
        except PortalUser.DoesNotExist:
            pass


class StaffResidentBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        email = kwargs['username']
        password = kwargs['password']
        try:
            staff_resident=StaffResident.objects.get(email=email)
            if staff_resident and check_password(password, staff_resident.password) is True:
                return staff_resident.email
        except StaffResident.DoesNotExist:
            pass