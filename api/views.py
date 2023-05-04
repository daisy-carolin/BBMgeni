from django.shortcuts import render
from subapp.models import*

# Create your views here.

from datetime import datetime
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from .models import User, VisitorLog, SecurityPersonnel, StaffResident, PortalUser, LocalAdmin, Branches,OrganisationalAdmin,Organisation,OrganisationCategory,CompanyCustomer,Invitation,Checker,SecurityRegistration,EmployeeRegistration,Roles,Purpose,Host,OrganisationCheckin

from .serializers import (
    VisitorLogSerializer,
    SecurityPersonnelSerializer,
    StaffResidentSerializer,
    PortalUserSerializer,
    LocalAdminSerializer,
    BranchesSerializer,
    UsersSerializer,
    HostSerializer,
    OrganisationalAdminSerializer,
    OrganisationSerializer,
    OrganisationCategorySerializer,
    CompanyCustomerSerializer,
    InvitationSerializer,
    CheckerSerializer,
    SecurityRegistrationSerializer,
    EmployeeRegistrationSerializer,
    RolesSerializer,
    PurposeSerializer,
    VisitorLogSerializer,
    StaffResidentSerializer,
    OrganisationCheckin,
    DynamicOrganisationSerializer
)

from drf_yasg.utils import swagger_auto_schema


from .serializers import *

from django.contrib.auth.hashers import make_password

# from .sms import SendSMS

# Create your views here.
class UsersView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersSerializer

    @swagger_auto_schema(responses={200: UsersSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        users = User.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=UsersSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = UsersSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class HostView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = HostSerializer

    @swagger_auto_schema(responses={200: HostSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        host = Host.objects.all()
        serializer = HostSerializer( host, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=HostSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = HostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class PortalUserView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PortalUserSerializer

    @swagger_auto_schema(responses={200: PortalUserSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        portal_user = PortalUser.objects.all()
        serializer = PortalUserSerializer( portal_user, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=PortalUserSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = PortalUserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SecurityPersonnelView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SecurityPersonnelSerializer

    @swagger_auto_schema(responses={200: SecurityPersonnelSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        security_Personnel = SecurityPersonnel.objects.all()
        serializer = SecurityPersonnelSerializer(security_Personnel, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=SecurityPersonnelSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = SecurityPersonnelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffResidentView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StaffResidentSerializer

    @swagger_auto_schema(responses={200: StaffResidentSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        staff_resident = SecurityPersonnel.objects.all()
        serializer = StaffResidentSerializer(staff_resident, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=StaffResidentSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = StaffResidentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LocalAdminView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LocalAdminSerializer

    @swagger_auto_schema(responses={200: LocalAdminSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        local_admin = LocalAdmin.objects.all()
        serializer = LocalAdminSerializer(local_admin, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=LocalAdminSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = LocalAdminSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class VisitortLogView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = VisitorLogSerializer

    @swagger_auto_schema(responses={200: VisitorLogSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        visitor_log = LocalAdmin.objects.all()
        serializer = VisitorLogSerializer(visitor_log, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=VisitorLogSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = VisitorLogSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class BranchesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = BranchesSerializer

    @swagger_auto_schema(responses={200: BranchesSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        branches = Branches.objects.all()
        serializer = BranchesSerializer(branches, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=BranchesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = BranchesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganisationalAdminView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganisationalAdminSerializer

    @swagger_auto_schema(responses={200: OrganisationalAdminSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        organisation_admin = OrganisationalAdmin.objects.all()
        serializer = OrganisationalAdminSerializer(organisation_admin , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OrganisationalAdminSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = OrganisationalAdminSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganisationView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganisationSerializer

    @swagger_auto_schema(responses={200: DynamicOrganisationSerializer(many=True)})
    def get(self, request, format=None, *args, **kwargs):
        organisation = Organisation.objects.all()
        serializer = DynamicOrganisationSerializer(organisation, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OrganisationSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = OrganisationSerializer(data=request.data, context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class OrganisationDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganisationSerializer

    @swagger_auto_schema(responses={200: DynamicOrganisationSerializer(many=False)})
    def get(self, request, format=None, *args, **kwargs):
        organisation = Organisation.objects.get(id=kwargs.get("pk"))
        print(organisation)
        serializer = DynamicOrganisationSerializer(organisation)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class OrganisationCategoryView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganisationCategorySerializer

    @swagger_auto_schema(responses={200: OrganisationCategorySerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        organisation_Category = OrganisationCategory.objects.all()
        serializer = OrganisationCategorySerializer( organisation_Category , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OrganisationCategorySerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = OrganisationCategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyCustomerView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CompanyCustomerSerializer

    @swagger_auto_schema(responses={200: CompanyCustomerSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        company_customer = CompanyCustomer.objects.all()
        serializer = CompanyCustomerSerializer( company_customer  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=CompanyCustomerSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = CompanyCustomerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class InvitationView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = InvitationSerializer

    @swagger_auto_schema(responses={200: InvitationSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        invitation = Invitation.objects.all()
        serializer = InvitationSerializer( invitation  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=InvitationSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = InvitationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            name = serializers.data.get("name")
            email=serializers.data.get("email")
            phone_number=serializers.data.get("phone_number")


            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class CheckerView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CheckerSerializer

    @swagger_auto_schema(responses={200: CheckerSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        invite_code = kwargs.get('invite_code', None)
        invitation = Invitation.objects.filter(invite_code=invite_code).first()
        if invitation is not None:
            serializer = InvitationSerializer(invitation)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            message = {
                "detail": "INVALID invite code."
            }
            return Response(status=status.HTTP_404_NOT_FOUND, data=message)



class SecurityRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SecurityRegistrationSerializer

    @swagger_auto_schema(responses={200:SecurityRegistrationSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        security_registration = SecurityRegistration.objects.all()
        serializer = SecurityRegistrationSerializer( security_registration  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=SecurityRegistrationSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = SecurityRegistrationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = EmployeeRegistrationSerializer

    @swagger_auto_schema(responses={200:EmployeeRegistrationSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        employee_registration = EmployeeRegistration.objects.all()
        serializer = EmployeeRegistrationSerializer( employee_registration  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=EmployeeRegistrationSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = EmployeeRegistrationSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class PurposeView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PurposeSerializer

    @swagger_auto_schema(responses={200:PurposeSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        purpose = Purpose.objects.all()
        serializer = PurposeSerializer( purpose  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=PurposeSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = PurposeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class RolesView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RolesSerializer

    @swagger_auto_schema(responses={200:RolesSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        roles= Roles.objects.all()
        serializer = RolesSerializer( roles  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=RolesSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = RolesSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class VisitorLogView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = VisitorLogSerializer

    @swagger_auto_schema(responses={200:VisitorLogSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        visitor_log= VisitorLog.objects.all()
        serializer = VisitorLogSerializer( visitor_log  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=VisitorLogSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = VisitorLogSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class StaffResidentView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = StaffResidentSerializer

    @swagger_auto_schema(responses={200:StaffResidentSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        staff_resident= StaffResident.objects.all()
        serializer = StaffResidentSerializer( staff_resident  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=StaffResidentSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = StaffResidentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganisationCheckinView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OrganisationCheckinSerializer

    @swagger_auto_schema(responses={200:OrganisationCheckinSerializer(many=True)})
    def get(self, format=None, *args, **kwargs):
        organisation_checkin= OrganisationCheckin.objects.all()
        serializer = OrganisationCheckinSerializer( organisation_checkin  , many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @swagger_auto_schema(request_body=OrganisationCheckinSerializer)
    def post(self, request, format=None, *args, **kwargs):
        serializers = OrganisationCheckinSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
