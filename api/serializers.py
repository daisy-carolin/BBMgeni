from ssl import Purpose
from rest_framework import serializers
from subapp.forms import Branches
from subapp.models import Checker, CompanyCustomer, EmployeeRegistration, Host, Invitation, LocalAdmin, Organisation, OrganisationCategory, OrganisationalAdmin, PortalUser, Roles, SecurityPersonnel, SecurityRegistration, StaffResident, User, VisitorLog
from .models import *
from rest_framework.validators import UniqueValidator
from subapp.models import User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "role", )


class VisitorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorLog
        fields = "__all__"


class SecurityPersonnelSerializer(serializers.ModelSerializer):
    user = UsersSerializer(many=False)

    class Meta:
        model = SecurityPersonnel
        fields = "__all__"


class StaffResidentSerializer(serializers.ModelSerializer):
    user = UsersSerializer(many=False)

    class Meta:
        model = StaffResident
        fields = "__all__"



class PortalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortalUser
        fields = "__all__"


class LocalAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalAdmin
        fields = "__all__"


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = "__all__"

class OrganisationalAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisationalAdmin
        fields = "__all__"


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"


class OrganisationCategorySerializer(serializers.ModelSerializer):
    user = UsersSerializer(many=False)

    class Meta:
        model = OrganisationCategory
        fields = "__all__"


class CompanyCustomerSerializer(serializers.ModelSerializer):
    user = UsersSerializer(many=False)

    class Meta:
        model = CompanyCustomer
        fields = "__all__"



class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = "__all__"


class CheckerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checker
        fields = "__all__"


class SecurityRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model =SecurityRegistration
        fields = "__all__"

class EmployeeRegistrationSerializer(serializers.ModelSerializer):
    user = UsersSerializer(many=False)

    class Meta:
        model = EmployeeRegistration
        fields = "__all__"



class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = "__all__"


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model =Host
        fields = "__all__"
