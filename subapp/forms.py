from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# we are creating forms for our users here
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
# class departmentForm(forms.ModelForm):
#     class Meta:
#         model = department
#         fields = '__all__'
#         widgets={
#             'user_id':forms.TextInput(attrs={'hidden':'hidden'}),
#         }
#     def __init__(self, *args, **kwargs):
#         super(departmentForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'
            
class HostForm(forms.ModelForm):
    
    class Meta:
        model = Host
        fields = '__all__'
        widgets={
            'user_id':forms.TextInput(attrs={'hidden':'hidden'}),
        }
    def __init__(self, *args, **kwargs):
        super(HostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PurposeForm(forms.ModelForm):
    class Meta:
        model = Purpose
        fields = '__all__'
        widgets={
            'user_id':forms.TextInput(attrs={'hidden':'hidden'}),
        }
    def __init__(self, *args, **kwargs):
        super(PurposeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
       
class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
          'role_name':forms.TextInput(attrs={'class':'form-control'}),
        #   'user_id':forms.TextInput(attrs={'hidden':'hidden'}),
        }
    def __init__(self, *args, **kwargs):
        super(RolesForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
            # visible.field.widget.attrs['class'] = 'form-control'
            
class CheckerEditForm(forms.ModelForm):
    class Meta:
        model = Checker
        fields = ['name','email','Phone_number','gender','in_time','out_time','note',]
        widgets={
            'name':forms.TextInput(attrs={'readonly':'readonly'}),
            'user_id':forms.TextInput(attrs={'hidden':'hidden'}),
            'visitor_id':forms.TextInput(attrs={'hidden':'hidden'}),
            'Phone_number':forms.TextInput(attrs={'readonly':'readonly'}),
            'email':forms.TextInput(attrs={'readonly':'readonly'}),
            'gender':forms.TextInput(attrs={'readonly':'readonly'}),
            'in_time':forms.TimeInput(attrs={'type': 'time','readonly':'readonly'}),
            'out_time':forms.TimeInput(attrs={'type': 'time'}),
        }
    def __init__(self, *args, **kwargs):
        super(CheckerEditForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
class CheckerForm(forms.ModelForm):
    class Meta:
        model = Checker
        fields = '__all__'
        widgets={
            'name':forms.TextInput(attrs={'readonly':'readonly'}),
            'visitor_id':forms.TextInput(attrs={'hidden':'hidden'}),
            'user_id':forms.TextInput(attrs={'hidden':'hidden'}),
            'Phone_number':forms.TextInput(attrs={'readonly':'readonly'}),
            'email':forms.TextInput(attrs={'readonly':'readonly'}),
            'gender':forms.TextInput(attrs={'readonly':'readonly'}),
            'in_time':forms.TimeInput(attrs={'type': 'time'}),
            'out_time':forms.TimeInput(attrs={'type': 'time','readonly':'readonly'}),
        }
    def __init__(self, *args, **kwargs):
        super(CheckerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class LocalAdminForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(LocalAdmin, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
            # visible.field.widget.attrs['class'] = 'form-control'

class Organisation(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
          'role_name':forms.TextInput(attrs={'class':'form-control'}),
          'role':forms.TextInput(attrs={'readonly':'readonly'}),
          'Phone_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'starting_date':forms.TextInput(attrs={'readonly':'readonly'}),
          'expiry_date':forms.TextInput(attrs={'readonly':'readonly'}),
          'category':forms.TextInput(attrs={'readonly':'readonly'}),
          'organisation_address':forms.TextInput(attrs={'readonly':'readonly'}),
          'postal_code':forms.TextInput(attrs={'readonly':'readonly'}),
          'postal_address':forms.TextInput(attrs={'readonly':'readonly'}),
          'location_address':forms.TextInput(attrs={'readonly':'readonly'}),
          'organisation_code':forms.TextInput(attrs={'readonly':'readonly'}),
}
    
    def __init__(self, *args, **kwargs):
        super(Organisation, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
         

class Branches(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
          'branch_name':forms.TextInput(attrs={'class':'form-control'}),
          'organisation':forms.TextInput(attrs={'readonly':'readonly'}),
          'location_address':forms.TextInput(attrs={'readonly':'readonly'}),
          'code':forms.TextInput(attrs={'readonly':'readonly'}),
          }
    
    def __init__(self, *args, **kwargs):
        super(Branches, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
         
class PortalUserForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
          'name':forms.TextInput(attrs={'class':'form-control'}),
          'department':forms.TextInput(attrs={'readonly':'readonly'}),
          'Phone_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'id_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'roles':forms.TextInput(attrs={'readonly':'readonly'}),
          'staff_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'status':forms.TextInput(attrs={'readonly':'readonly'}),
          }
    
    def __init__(self, *args, **kwargs):
        super(PortalUser, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
         
class StaffResidentForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
          'name':forms.TextInput(attrs={'class':'form-control'}),
          'department':forms.TextInput(attrs={'readonly':'readonly'}),
          'Phone_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'id_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'roles':forms.TextInput(attrs={'readonly':'readonly'}),
          'staff_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'status':forms.TextInput(attrs={'readonly':'readonly'}),
          }
    
    def __init__(self, *args, **kwargs):
        super(StaffResident, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
         

class SecurityPersonnelForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
          'name':forms.TextInput(attrs={'class':'form-control'}),
          'department':forms.TextInput(attrs={'readonly':'readonly'}),
          'Phone_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'id_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'roles':forms.TextInput(attrs={'readonly':'readonly'}),
          'staff_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'status':forms.TextInput(attrs={'readonly':'readonly'}),
          }
    
    def __init__(self, *args, **kwargs):
        super(PortalUser, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'

class HomeScreen(forms.ModelForm):
    class Meta:
        model=HomeScreen
        fields = '__all__'
        widgets={
            'email':forms.TextInput(attrs={'readonly':'readonly'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),

        }


class OrganisationAdminalForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
          'name':forms.TextInput(attrs={'class':'form-control'}),
          'code':forms.TextInput(attrs={'readonly':'readonly'}),
          'Phone_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'category':forms.TextInput(attrs={'readonly':'readonly'}),
          'start_date':forms.TextInput(attrs={'readonly':'readonly'}),
          'expiry_date':forms.TextInput(attrs={'readonly':'readonly'}),
          'organisation_address':forms.TextInput(attrs={'readonly':'readonly'}),
          'maximum_branch':forms.TextInput(attrs={'readonly':'readonly'}),
        #   'organisational_fields':forms.MultipleChoiceField(choices=ORGANISATINAL_CHOICES),
          }
    
    def __init__(self, *args, **kwargs):
        super(OrganisationalAdmin, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
         

class VisitorLogForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
          'name':forms.TextInput(attrs={'class':'form-control'}),
          'host':forms.TextInput(attrs={'readonly':'readonly'}),
          'Phone_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'id_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'checkin_time':forms.TextInput(attrs={'readonly':'readonly'}),
          'checkout_time':forms.TextInput(attrs={'readonly':'readonly'}),
          'vehicle_number':forms.TextInput(attrs={'readonly':'readonly'}),
          'company_name':forms.TextInput(attrs={'readonly':'readonly'}),
          'pax':forms.TextInput(attrs={'readonly':'readonly'}),
          'checkin_from':forms.TextInput(attrs={'readonly':'readonly'}),
          }
          
    def __init__(self, *args, **kwargs):
        super(VisitorLogForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-check-input'
         

class UserAccessForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets={
}


class WebCheckingForm(forms.ModelForm):
    class Meta:
        model = VisitorLog
        fields = "__all__"

class OrganisationCheckinForm(forms.ModelForm):
    class Meta:
        model = OrganisationCheckin
        fields = "__all__"