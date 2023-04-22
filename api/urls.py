from django.urls import path
from . import views

    
urlpatterns = [
    path('users', views.UsersView.as_view(),name='users'),
    path('visitor_log', views.VisitorLogView.as_view(),name='visitor_log'),
    path('security_personnel', views.SecurityPersonnelView.as_view(),name='security_personnel'),
    path('staff_resident', views.StaffResidentView.as_view(),name='staff_resident'),
    path('portal_user', views.PortalUserView.as_view(),name='portal_user'),
    path('purpose', views.PurposeView.as_view(),name='purpose'),
    path('roles', views.RolesView.as_view(),name='roles'),
    path('employee_resgistration', views.EmployeeRegistrationView.as_view(),name='employee_registration'),
    path('security_resgistration', views.SecurityRegistrationView.as_view(),name='security_registration'),
    path('checker', views.CheckerView.as_view(),name='checker'),
    path('invitation', views.InvitationView.as_view(),name='invitation'),
    path('company_customer', views.CompanyCustomerView.as_view(),name='company_customer'),
    path('organisation_category', views.OrganisationCategoryView.as_view(),name='organisation_category'),
    path('organisation', views.OrganisationView.as_view(),name='organisation'),
    path('organisational_admin', views.OrganisationalAdminView.as_view(),name='organisational_admin'),
    path('host', views.HostView.as_view(),name='host'),
    path('branches', views.BranchesView.as_view(),name='branches'),
    path('local_admin', views.LocalAdminView.as_view(),name='local_admin'),


]


