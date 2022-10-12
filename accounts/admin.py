# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# from .models import CustomUser, CustomUserAdmin
# from django.views.generic import ListView, DetailView, TemplateView
# from django.contrib.auth.models import User
# # from accounts.managers import CustomUserManager
# # admin.site.unregister(User)
# # # Remove Group Model from admin. We're not using it.

# from my_user_profile_app.models import Employee
# # Define an inline admin descriptor for Employee model
# # which acts a bit like a singleton
# class EmployeeInline(admin.StackedInline):
#     model = Employee
#     can_delete = False
#     verbose_name_plural = 'employee'
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (EmployeeInline,)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

# # admin.site.register(CustomUser, CustomUserAdmin)