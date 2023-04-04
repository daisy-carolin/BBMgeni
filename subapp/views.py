from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .check_user_role import check_role_is_localadmin_and_staffresident_and_portaluser, check_role_is_organisationadmin_and_localadmin, check_role_is_organisational_admin,check_role_is_portal_user, check_role_is_security, check_role_is_staffresident
import random, string
# from .sms import SendSMS
from .email import send_email
from postmarker.core import PostmarkClient
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

User = get_user_model()

# Create your views here.
def unique_id(pre, suf):
    tot_rec_count = len(suf) + 1
    if len(str(tot_rec_count)) == 1:
        id = pre + "00" + str(tot_rec_count)
    elif len(str(tot_rec_count)) == 2:
        id = pre + "0" + str(tot_rec_count)
    else:
        id = pre + str(tot_rec_count)
    return id

@login_required(login_url='/login',)
@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def home(request):
    return render(request, "dashboard.html")


# def Department(request):
#     records=department.objects.all()
#     form = departmentForm(initial={'user_id':request.user.id})
#     if request.method=='POST':
#         form= departmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print('This valid and saved')
#             return redirect('Department')
#         else:
#             print(form.errors)
#     context={
#         'form':form,'records':records,'department':'active'
#     }
#     return render(request,'mgeni/department.html',context)



def login_user(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(request,username=username,password=password)
    print(user)
    if user is not None:
        print(f"User in role {user.role}")
        login(request,user)
        return redirect('home')
     
    return render(request, "mgeni/login_user.html")



def logout_view(request):
    logout(request)
    return redirect('/login')

def webcheckin_view(request):
    if request.method == "POST":
        a = VisitorLog(
                visitor_name=request.POST.get("username"),
                host=request.POST.get("role"),
                phone_number=request.POST.get("phone_number"),
                company_name=request.POST.get("company_name"),
                id_number=request.POST.get("id_number"),
                pax=request.POST.get("pax"),
                checkin_time=request.POST.get("checkin_time"),
                checkout_time=request.POST.get("checkout_time"),
                vehicle_number=request.POST.get("vehicle_number"),
                checkin_from="Web Checkin",
                is_in=True 
            )
        a.save()
        return redirect("visitorlog")
    return render(request, "mgeni/webcheckin.html")

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def host(request):
    records = Host.objects.all()
    form = HostForm(initial={"user_id": request.user.id})
    if request.method == "POST":
        form = HostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("host")
        else:
            print(form.errors)
    context = {"form": form, "records": records, "host": "active"}
    return render(request, "mgeni/host.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def purpose(request):
    records = Purpose.objects.all()
    form = PurposeForm(initial={"user_id": request.user.id})
    if request.method == "POST":
        form = PurposeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("purpose")
        else:
            print(form.errors)
    context = {"form": form, "records": records, "purpose": "active"}
    return render(request, "mgeni/purpose.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def roles(request):
    records = Roles.objects.all()

    context = {"records": records, "roles": "active"}
    return render(request, "mgeni/roles.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def add_roles(request):
    form = RolesForm(initial={"user_id": request.user.id})
    if request.method == "POST":
        form = RolesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("roles")
        else:
            print(form.errors)
    context = {"form": form, "roles": "active"}
    return render(request, "mgeni/add_roles.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def edit_roles(request, pk):
    record = Roles.objects.get(id=pk)
    form = RolesForm(instance=record)
    if request.method == "POST":
        form = RolesForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("roles")
        else:
            print(form.errors)
    context = {"form": form, "roles": "active"}
    return render(request, "mgeni/add_roles.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def delete_roles(request, pk):
    Roles.objects.get(id=pk).delete()
    return redirect("roles")

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def employee_registration(request):
    records = EmployeeRegistration.objects.all()
    context = {"employee": "active", "records": records}
    return render(request, "mgeni/registration.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def employee_registration_add(request):
    suf = EmployeeRegistration.objects.all()
    roles = Roles.objects.all()
    host = Host.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        username = request.POST.get("username")
        if form.is_valid():
            form.save()
            user_name = User.objects.filter(username=username).first()
            a = EmployeeRegistration(
                user_id_id=request.user.id,
                register_user_id_id=user_name.id,
                register_id=unique_id("RID", suf),
                name=request.POST.get("username"),
                phone=request.POST.get("phone_number"),
                email=request.POST.get("email"),
                gender=request.POST.get("gender"),
                image=request.FILES.get("image"),
                address=request.POST.get("address"),
                city=request.POST.get("city"),
                country=request.POST.get("country"),
                postal_code=request.POST.get("postal_code"),
                id_proof_type=request.POST.get("proof_type"),
                id_proof_image=request.FILES.get("proof"),
                description=request.POST.get("description"),
                role_id=request.POST.get("role"),
                host_id=request.POST.get("host"),
                status="Active",
            )
            a.save()
            return redirect("employee_registration")
    context = {"employee": "active", "form": form, "roles": roles, "host": host}
    return render(request, "mgeni/registration_add.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def security_registration(request):
    records = SecurityRegistration.objects.all()
    context = {"security": "active", "records": records}
    return render(request, "mgeni/security_registration.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def security_registration_add(request):
    suf = SecurityRegistration.objects.all()
    roles = Roles.objects.all()
    host = Host.objects.all()
    form = CreateUserForm(request.POST)
    if request.method == "POST":
        name = request.POST.get("username")

        user = User.objects.create(
            email=request.POST.get("email"),
            password=make_password(request.POST.get("password")), 
            role=roles.get(role_name ="SecurityPersonnel"),       )
        
        user_name = User.objects.filter(email=name).first()
        a = SecurityPersonnel(
            user=user,
                name=request.POST.get("name"),
                phone_number=request.POST.get("phone_number"),
                email = request.POST.get("email"),
                department=request.POST.get("department"),
                staff_number=request.POST.get("staff_number"),
                # role_id=request.POST.get("role"),
                status="Active"
        )
        return redirect("security_registration_add")
    context = {
        "security_registration_add": "active",
        "form": form,
        "roles": roles,
        "host": host,
    }
    return render(request, "mgeni/security_registration_add.html", context)

def invitation(request):
    records = Invitation.objects.all()
    context = {"security": "active", "records": records}
    return render(request, "mgeni/invitation.html", context)

def invitation_add(request):
    save_btn = request.POST.get("save")
    send_btn = request.POST.get("send")
    inv_records = Invitation.objects.all().count()
    current_datetime = datetime.now()
    invitation_id = (
        "IVID"
        + str(current_datetime.strftime("%Y"))
        + str(current_datetime.strftime("%m"))
        + str(current_datetime.strftime("%d"))
        + str(inv_records)
    )
    print(invitation_id, save_btn)
    if request.method == "POST":
        if save_btn:
            invite_code = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
            Invitation.objects.create(
                invitation_id=invitation_id,
                visitor_id="",
                name=request.POST.get("name"),
                phone_number=request.POST.get("phone_number"),
                email=request.POST.get("email"),
                meeting_time=request.POST.get("meeting_time"),
                meeting_date=request.POST.get("meeting_date"),
                meeting_duration_time=request.POST.get("meeting_duration_time"),
                purpose_of_meeting=request.POST.get("purpose_of_meeting"),
                invite_code = invite_code
            )
            name = request.POST.get("name")
            meeting_date = request.POST.get("meeting_date")
            meeting_time=request.POST.get("meeting_time"),
            email=request.POST.get("email"),

            messages.success(request, "Sucessfully Invitation is saved")
            # SendSMS().send(
            #     phone_number=request.POST.get("phone_number"),
            #     meeting_date=request.POST.get("meeting_date"),
            #     meeting_time=request.POST.get("meeting_time"),
            #     invite_code=invite_code,
            #     name=request.POST.get("name")
            #     )
            postmark = PostmarkClient(server_token='92895c56-a7c3-4525-8a99-0bc297b6d354')
            postmark.emails.send(
                From= "rmbugua@mgeniapp.com",
                To= email,
                Subject= "Meeting Invitation",
                HtmlBody= f"Hello {name} \n Your invitstion code is {invite_code}, \nMeeting Date: {meeting_date} \nMeeting time: {meeting_time}",
                MessageStream="message"
            )   

            
        elif send_btn:
            # we want to intergrate with mail
            Invitation.objects.create(
                invitation_id=invitation_id,
                visitor_id="",
                name=request.POST.get("name"),
                phone_number=request.POST.get("phone_number"),
                email=request.POST.get("email"),
                meeting_time=request.POST.get("meeting_time"),
                meeting_date=request.POST.get("meeting_date"),
                meeting_duration_time=request.POST.get("meeting_duration_time"),
                purpose_of_meeting=request.POST.get("purpose_of_meeting"),
                status="Accepted",
            )
            messages.success(request, "Sucessfully Invitation is send")
        return redirect("invitation")
    context = {"invitation": "active", "invitation_id": invitation_id}
    return render(request, "mgeni/invitation_add.html", context)

@user_passes_test(check_role_is_security)
def checker(request):
    print(request.user.role)
    # today_min = datetime.combine(datetime.date.today(), datetime.time.min)
    # today_max = datetime.combine(datetime.date.today(), datetime.time.max)
    # check_in=Security_Validation.objects.filter(created_at__range=(today_min, today_max),out_time=None) #toaday record
    # check_in = Checker.objects.filter(out_time=None)
    check_record = None
    form = CheckerForm()
    # save = request.POST.get("save1")
    search_btn = request.POST.get("search_btn")
    if search_btn:
        name = request.POST.get("search")
        check_record = Invitation.objects.filter(invite_code=name).first()
        print(check_record)

        
        return redirect("visitor_log.html")

    context = {"form": form, "check_in": check_record}
    return render(request, "mgeni/checker.html", context)



@user_passes_test(check_role_is_security)
def checker_edit(request, pk):
    check_record = Checker.objects.get(id=pk)
    form = CheckerEditForm(instance=check_record)
    if request.method == "POST":
        form = CheckerEditForm(request.POST, instance=check_record)
        if form.is_valid():
            form.save()
            return redirect("checker")
        else:
            print(form.errors)
    context = {
        "form": form,
    }
    return render(request, "mgeni/checker_edit.html", context)


# def vistior_log(request):
#     records=vistior_log.objects.all()
#     context = {"vistior_records": "active", "records": records}
#     return render(request, "mgeni/vistior_log.html", context)


def company_customer(request):
    records = CompanyCustomer.objects.all()
    context = {"vistior_records": "active", "records": records}
    return render(request, "mgeni/company_customer.html", context)


def company_customer_add(request):
    records = CompanyCustomer.objects.all()
    context = {"vistior_records": "active", "records": records}
    return render(request, "mgeni/company_customer_add.html", context)

@user_passes_test(check_role_is_organisational_admin)
def local_admin_log(request):
    records = LocalAdmin.objects.all()
    context = {"local_admin_records": "active", "records": records}
    return render(request, "mgeni/local_admin_log.html", context)

@user_passes_test(check_role_is_organisational_admin)
def local_admin_add(request):
    suf = LocalAdmin.objects.all()
    roles = Roles.objects.all()
    host = Host.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        name = request.POST.get("name")

        user = User.objects.create(
            email=request.POST.get("email"),
            password=make_password(request.POST.get("password")),
            role=roles.get(role_name ="LocalAdmin"),
      )

      
        LocalAdmin.objects.create(
            user=user,
            name=request.POST.get("name"),
            phone_number=request.POST.get("phone_number"),
            email=request.POST.get("email"),
        )
           
        return redirect("local_admin_add")
    context = {
        "local_admin_add": "active",
        "form": form,
        "roles": roles,
        "host": host,
    }
    return render(request, "mgeni/local_admin_add.html", context)



def roles(request):
    records = Roles.objects.all()
    context = {"roles_records": "active", "records": records}
    return render(request, "mgeni/roles.html", context)


def organisation(request):
    records = Organisation.objects.all()
    context = {"organisation_records": "active", "records": records}
    return render(request, "mgeni/organisation.html", context)

def organisation_add(request):
    suf =Organisation.objects.all()
    roles = Roles.objects.all()
    host = Host.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            a = Organisation(
                organisation_name=request.POST.get("username"),
                role=request.POST.get("role"),
                phone_number = request.POST.get("phone_number"),
                starting_date = request.POST.get("starting_date"),
                organisation_category=request.POST.get("organisation_category"),
                organisational_address=request.POST.get("organisational_address"),
                postal_code=request.POST.get("postal_code"),
                postal_address=request.POST.get("postal_address"),
                location_address=request.POST.get("location_address"),
                organisation_code=request.POST.get("organisation_code"),


                status="Active",
            )
            a.save()
            return redirect("organisation_registration")
    context = {"organisation": "active", "form": form, "roles": roles, "host": host}
    return render(request, "mgeni/organisation_add.html", context)


def branches(request):
    records = Branches.objects.all()
    context = {"branches_records": "active", "records": records}
    return render(request, "mgeni/branches_log.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def portaluser(request):
    records = PortalUser.objects.all()
    context = {"portal_user_records": "active", "records": records}
    return render(request, "mgeni/portal_user.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def portal_user_add(request):
    suf = PortalUser.objects.all()
    roles = Roles.objects.all()
    host = Host.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        username = request.POST.get("username")

        user = User.objects.create(
            email=request.POST.get("email"),
            password=make_password(request.POST.get("password")),
            role=roles.get(role_name ="PortalUser"),

        )
       
        PortalUser.objects.create(
                user=user,
                name=request.POST.get("name"),
                department=request.POST.get("department"),
                email = request.POST.get("email"),
                id_number=request.POST.get("id_number"),
                phone_number=request.POST.get("phone_number"),
                staff_number=request.POST.get("staff_number"),
                status="Active",
            )
        return redirect("portal_user_add")
    context = {
        "portal_user_add": "active",
        "form": form,
        "roles": roles,
        "host": host,
    }
    return render(request, "mgeni/portal_user_add.html", context)


@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def staff_residential(request):
    records = StaffResident.objects.all()
    context = {"staff_residential_records": "active", "records": records}
    return render(request, "mgeni/staff_residential.html", context)

@user_passes_test(check_role_is_organisationadmin_and_localadmin)
def staff_residential_add(request):
    suf = StaffResident.objects.all()
    roles = Roles.objects.all()
    host = Host.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        name = request.POST.get("username")

        user = User.objects.create(
            email=request.POST.get("email"),
            password=make_password(request.POST.get("password")),
            role=roles.get(role_name ="Staff/Resident"),


        )

        StaffResident.objects.create(
                user=user,
                name=request.POST.get("name"),
                phone_number=request.POST.get("phone_number"),
                email = request.POST.get("email"),
                department=request.POST.get("department"),
                staff_number=request.POST.get("staff_number"),
                role_id=request.POST.get("role"),
                status="Active",
            )
        
        return redirect("staff_residential_add")
    context = {
        "staff_residential_add": "active",
        "form": form,
        "roles": roles,
        "host": host,
    }
    return render(request, "mgeni/staff_residential_add.html", context)




def organisation_admin_log(request):
    records = OrganisationalAdmin.objects.all()
    print(records)
    context = {"organisation_admin_log_records": "active", "records": records}
    return render(request, "mgeni/organisation_admin_log.html", context)

def organisation_admin_add(request):
    suf = OrganisationalAdmin.objects.all()
    roles = Roles.objects.all()
    host = Host.objects.all()
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        name = request.POST.get("username")

        user = User.objects.create(
            email=request.POST.get("email"),
            password=make_password(request.POST.get("password")),
            role=roles.get(role_name ="OrganisationAdmin"),
        )

        
        OrganisationalAdmin.objects.create(
            user=user,
            name=request.POST.get("name"),
            phone_number=request.POST.get("phone_number"),
            category=request.POST.get("category"),
            start_date=request.POST.get("start_date"),
            expiry_date=request.POST.get("expiry_date"),
            organisational_address=request.POST.get("organisational_address"),
            maximum_branch=request.POST.get("maximum_branch"),
        )

        return redirect("organisation_admin_add")
    context = {
        "organisation_admin_add": "active",
        "form": form,
        "roles": roles,
        "host": host,
    }
    return render(request, "mgeni/organisation_admin_add.html", context)



    
       

def visitorlog(request):
    visitors = VisitorLog.objects.all()
    context = {"visitors": visitors}

    return render(request, "mgeni/visitorlog.html", context)



