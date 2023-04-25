from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login_user,name='login_user'),
    path('host', views.host,name='host'),
    path('purpose', views.purpose,name='purpose'),
    path('roles', views.roles,name='roles'),
    path('add_roles', views.add_roles,name='add_roles'),
    path('edit_roles/<pk>', views.edit_roles,name='edit_roles'),
    path('delete_roles/<pk>', views.delete_roles,name='delete_roles'),
    path('employee_registration', views.employee_registration,name='employee_registration'),
    path('employee_registration_add', views.employee_registration_add,name='employee_registration_add'),
    path('security_registration', views.security_registration,name='security_registration'),
    path('security_registration_add', views.security_registration_add,name='security_registration_add'),
    path('invitation', views.invitation,name='invitation'),
    path('invitation_add',views.invitation_add, name='invitation_add'),
    path('checker',views.checker, name='checker'),
    path('checker_edit/<pk>',views.checker_edit, name='checker_edit'),
    path('visitorlog',views.visitorlog, name='visitorlog'),
    path('company_customer',views.company_customer, name='company_customer'),
    path('company_customer_add',views.company_customer_add, name='company_customer_add'),
    path('local_admin_log',views.local_admin_log, name='local_admin_log'),
    path('local_admin_add',views.local_admin_add, name='local_admin_add'),
    path('organisation_admin_log',views.organisation_admin_log, name='organisation_admin_log'),
    path('organisation_admin_add',views.organisation_admin_add, name='organisation_admin_add'),
    path('staff_residential',views.staff_residential, name='staff_residential'),
    path('staff_residential_add',views.staff_residential_add, name='staff_residential_add'),
    path('portaluser',views.portaluser, name='portaluser'),
    path('portal_user_add',views.portal_user_add, name='portal_user_add'),
    path('logout/', views.logout_view, name='logout'),
    path('webcheckin/', views.webcheckin_view, name='webcheckin'),
    path('organisationcheckin/', views.organisation_checkin, name='organisationcheckin'),


]