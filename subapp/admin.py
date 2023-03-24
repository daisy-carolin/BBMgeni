from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

# admin.site.register(department)
class CustomUserAdmin(UserAdmin):
    search_fields = ('email', )
    ordering = ('-created_on', )
    list_filter = ('email', 'is_active', 'is_staff', )
    list_display = ('email', 'is_active', 'is_staff', )

    fieldsets = (
        ('Personal', {'fields': ('email', 'password', )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email','password1', 'password2', 'is_active', 'is_staff', 'is_superuser', ),
        }),
    )

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Roles)
admin.site.register(Host)
admin.site.register(EmployeeRegistration)
admin.site.register(Checker)
admin.site.register(Invitation)
admin.site.register(Unappoinment_visit)
admin.site.register(LocalAdmin)
admin.site.register(OrganisationalAdmin)
admin.site.register(Branches)
admin.site.register(OrganisationCategory)
admin.site.register(PortalUser)
admin.site.register(StaffResident)
admin.site.register(SecurityPersonnel)
admin.site.register(HomeScreen)
admin.site.register(Organisation)
