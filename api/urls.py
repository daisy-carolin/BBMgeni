from django.urls import path
from . import views

    
urlpatterns = [
    path('users', views.UsersView.as_view(),name='users_api'),
    path('visitor_log', views.VisitorLogView.as_view(),name='visitor_log_api'),
    path('security_personnel', views.SecurityPersonnelView.as_view(),name='security_personnel_api'),
    path('staff_resident', views.StaffResidentView.as_view(),name='staff_resident_api'),
    path('portal_user', views.PortalUserView.as_view(),name='portal_user_api'),
    path('purpose', views.PurposeView.as_view(),name='purpose_api'),
    path('roles', views.RolesView.as_view(),name='roles_api'),
    path('employee_resgistration', views.EmployeeRegistrationView.as_view(),name='employee_registration_api'),
    path('security_resgistration', views.SecurityRegistrationView.as_view(),name='security_registration_api'),
    path('checker/<invite_code>', views.CheckerView.as_view(),name='checker_api'),
    path('invitation', views.InvitationView.as_view(),name='invitation_api'),
    path('company_customer', views.CompanyCustomerView.as_view(),name='company_customer_api'),
    path('organisation_category', views.OrganisationCategoryView.as_view(),name='organisation_category_api'),
    path('organisation', views.OrganisationView.as_view(),name='organisation_api'),
    path('organisation/<int:pk>', views.OrganisationDetailView.as_view(),name='organisation_detail_api'),
    path('organisational_admin', views.OrganisationalAdminView.as_view(),name='organisational_admin_api'),
    path('host', views.HostView.as_view(),name='host_api'),
    path('branches', views.BranchesView.as_view(),name='branches_api'),
    path('local_admin', views.LocalAdminView.as_view(),name='local_admin_api'),
    path('organisation_checkin', views.OrganisationCheckinView.as_view(),name='organisation_checkin_api'),
    path('checkout', views.CheckoutView.as_view(), name='checkout_api'),
    path('check_id_vehicle_number', views.VisitorLogView1.as_view(), name='check_id_vehicle_number'),




]


