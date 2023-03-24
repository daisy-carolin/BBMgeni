from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, password, **other_fields)

    
    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide a valid email address'))

        email = self.normalize_email(email)
        user = self.model(email=email,  **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    class Types(models.TextChoices):
        ORGANISATION_ADMIN= "ORGANISATION_ADMIN" , "ORGANISATION_ADMIN"
        LOCAL_ADMIN = "LOCAL_ADMIN" , "LOCAL_ADMIN"
        PORTAL_USER = "PORTAL_USER " , "PORTAL_USER"
        STAFF_RESIDENT = "  STAFF_RESIDENT" , "STAFF_RESIDENT"
        SECURITY_PERSONEL = "SECURITY_PERSONEL" , "SECURITY_PERSONEL"
    
          
    type = models.CharField(max_length = 30 , choices = Types.choices , 
                            # Default is user is staff_resident
                            default = Types.STAFF_RESIDENT)

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=30, null=True, blank=False)
    last_name = models.CharField(max_length=30, null=True, blank=False)
    is_organisationadmin= models.BooleanField(default = False)
    is_localadmin = models.BooleanField(default = False)
    is_portaluser = models.BooleanField(default = False)
    is_staffresident= models.BooleanField(default = False)
    is_securitypersonel = models.BooleanField(default = False)
    created_on = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def _str_(self) -> str:
        return self.email




# Create your models here.
class Host(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    status=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    
class HomeScreen(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    def __str__(self):
        return str(self.password)


class Purpose(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    status=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)

class Roles(models.Model):
    # user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    role_name=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 

    # registration_add=models.BooleanField()
    # registration_edit=models.BooleanField()
    # registration_delete=models.BooleanField()
    # invitation_create=models.BooleanField()
    # invitation_send=models.BooleanField()
    # vistior_log=models.BooleanField()
    # check_in_and_out=models.BooleanField()
    def __str__(self):
        return str(self.role_name)
    
class EmployeeRegistration(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='example3')
    register_user_id=models.ForeignKey(User,related_name='example4',on_delete=models.CASCADE,null=True)
    register_id=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    image=models.FileField(upload_to='images/',blank=True, null=True)
    address=models.CharField(max_length=100,blank=True, null=True)
    city=models.CharField(max_length=100,blank=True, null=True)
    country=models.CharField(max_length=100,blank=True, null=True)
    postal_code=models.CharField(max_length=100,blank=True, null=True)
    id_proof_type=models.CharField(max_length=100,blank=True, null=True)
    id_proof_image=models.FileField(upload_to='images/',blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    #department = models.ForeignKey(department,on_delete=models.CASCADE,blank=True, null=True)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE,blank=True, null=True)
    host = models.ForeignKey(Host,on_delete=models.CASCADE,blank=True, null=True)
    status=models.CharField(max_length=100,blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

class SecurityRegistration(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    invite_time=models.TimeField(null=True)
    invite_date=models.DateField(null=True)
    id_number=models.CharField(max_length=100)
    vehicle_number=models.CharField(max_length=100, null=True)

class Checker(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    visitor_id= models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    Phone_number= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    in_time=models.TimeField()
    out_time=models.TimeField(blank=True,null=True)
    note= models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)
    
class Invitation(models.Model):
    invitation_id=models.CharField(max_length=100)
    visitor_id= models.CharField(max_length=100,blank=True,null=True)
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    meeting_time=models.TimeField()
    meeting_date=models.DateField()
    meeting_duration_time=models.IntegerField()
    purpose_of_meeting=models.TextField()
    invite_code=models.CharField(max_length=5, null=True, blank=False)
    
    class StatusChoice(models.TextChoices):
        WAITING = 'Waiting', 'Waiting'
        ACCEPTED = 'Accepted', 'Accepted'

    status=models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.WAITING)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class CompanyCustomer(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, null=True,related_name='example5')
    customer_user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True,related_name='example6')
    customer_id = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    start_date = models.DateField()
    expiry_date = models.DateField()
    no_of_department = models.IntegerField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
class OrganisationCategory(models.Model): 
    category_name = models.CharField(max_length=100)
    category_code=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.category_name

class Organisation(models.Model):
    organisation_name=models.CharField(max_length=100)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE,blank=True, null=True)
    phone_number=models.CharField(max_length=100,blank=True,null=True)
    starting_date=models.DateField()
    expiry_date=models.DateField()
    organisation_category=models.ForeignKey(OrganisationCategory, on_delete=models.CASCADE)
    organisational_address=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=100)
    postal_address=models.CharField(max_length=100)
    location_address=models.CharField(max_length=100)
    organisation_code=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.organisation_name

class OrganisationalAdmin(models.Model):
    name=models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True, blank=False, unique=True, db_index=True)
    role = models.CharField(max_length=25,  default="Organisation Admin", null=True)
    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE, null=True)
    phone_number=models.CharField(max_length=100,blank=True,null=True)
    category=models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    expiry_date = models.DateField(null=True)
    maximum_branch=models.CharField(max_length=100)
    organisational_address=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=100)
    password = models.CharField(max_length=250, null=True, blank=False)

    

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(OrganisationalAdmin, self).save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.organisational_address

# class department(models.Model):
#     organisation_admin=models.ForeignKey(OrganisationalAdmin,on_delete=models.CASCADE, null=True)
#     name=models.CharField(max_length=100,blank=True,null=True)
#     status=models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.name)

class Branches(models.Model): 
    branch_name = models.CharField(max_length=100)
    organisation = models.OneToOneField(Organisation, on_delete=models.CASCADE)
    organisational_admin = models.ForeignKey(OrganisationalAdmin,on_delete=models.CASCADE, null=True)
    location_address=models.CharField(max_length=100)
    code=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.branch_name


class LocalAdmin(models.Model): 
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, blank=False, unique=True, db_index=True)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE, null=True)
    branch = models.ForeignKey(Branches,on_delete=models.CASCADE, null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=255, null=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(LocalAdmin, self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.customer_name

class PortalUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=False, unique=True, db_index=True)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE, null=True)
    localAdmin = models.ForeignKey(LocalAdmin,on_delete=models.CASCADE, null=True)
    department= models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    staff_number = models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    password = models.CharField(max_length=250, null=True, blank=False)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(PortalUser, self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.staff_number
    
class StaffResident(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=False, unique=True, db_index=True)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE, null=True)
    localAdmin = models.ForeignKey(LocalAdmin,on_delete=models.CASCADE, null=True)
    department= models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    staff_number = models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    password = models.CharField(max_length=250, null=True, blank=False)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(StaffResident, self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.department
    
class SecurityPersonnel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=False, unique=True, db_index=True)
    role = models.ForeignKey(Roles,on_delete=models.CASCADE, null=True)
    localAdmin = models.ForeignKey(LocalAdmin,on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    invite_date=models.DateField()
    invite_time=models.TimeField()
    vehicle_number = models.CharField(max_length=100, null=True)
    id_number = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=250, null=True, blank=False)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(SecurityPersonnel, self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.purpose
          
      
class Unappoinment_visit(models.Model):
    visitor_id = models.CharField(max_length=100)
    security_id = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number=models.CharField(max_length=100,blank=True,null=True)
    email=models.CharField(max_length=100,blank=True,null=True)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=100)
    id_proof_type=models.CharField(max_length=100)
    id_proof_image=models.FileField(upload_to='images/')
    meeting_time=models.TimeField()
    meeting_date=models.DateField()
    meeting_duration_time=models.IntegerField()
    purpose_of_meeting=models.TextField()
    status=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class VisitorLog(models.Model):
    visitor_name = models.CharField(max_length=100)
    host = models.ForeignKey(Roles,on_delete=models.CASCADE, null=True)
    phone_number = models.CharField(max_length=100)
    id_number=models.CharField(max_length=100,blank=True,null=True)
    company_name=models.CharField(max_length=100)
    checkin_time=models.DateField()
    checkout_time=models.TimeField()
    checkin_from=models.TimeField()
    vehicle_number = models.CharField(max_length=100, null=True)
    pax = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.purpose