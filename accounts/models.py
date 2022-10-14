from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, default='', unique=True)
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    username = models.CharField(max_length=255, blank=True, default='', unique=True)
    CUSTOMER = 'Customer'
    AGENT = 'Agent'
    MANAGER = 'Manager'
    ROLE_CHOICES = [
        (CUSTOMER,'Customer'), 
        (AGENT, 'Agent'), 
        (MANAGER,'Manager'),
        ]

    role = models.CharField(
        max_length=255,
        choices=ROLE_CHOICES,
        blank=True, 
        null=True, 
        default=CUSTOMER)
      # You can create Role model separately and add ManyToMany if user has more than one role

# class User(AbstractUser):
#     """
#     Users within the Django authentication system are represented by this
#     model.

#     Username and password are required. Other fields are optional.
#     """
#     def create_user(self, email, username, first_name, last_name, group, password, **extra_fields):
#         if not email:
#             raise ValueError('Your Email must be set')
#         email = self.normalized_email(email)
#         if not username:
#             raise ValueError('Your Username must be set')
#         username = models.CharField(verbose_name='username', max_length=255, unique=True)
#         email = models.EmailField( verbose_name='email address', max_length=255, unique=True)
#         first_name = models.CharField( verbose_name='first name', max_length=255, unique=False)
#         last_name = models.CharField( verbose_name='last name', max_length=255, unique=False)
#         is_active = models.BooleanField(default=True)
#         is_staff = models.BooleanField(default=False)
#         date_joined = models.DateTimeField(auto_now_add=True)
#         user = self.model(
#             email=email,
#             usernam=username,
#             first_name=first_name,
#             last_name=last_name,
#             group=group
#             **extra_fields,
#             )
#         user.set_password(password)
#         user.save()
#         return user
#     class Meta(AbstractUser.Meta):
#         swappable = "AUTH_USER_MODEL"

# class CustomUser(AbstractBaseUser, PermissionRequiredMixin):
#     username = models.CharField(verbose_name='username', max_length=255, unique=True)
#     email = models.EmailField( verbose_name='email address', max_length=255, unique=True)
#     first_name = models.CharField( verbose_name='first name', max_length=255, unique=False)
#     last_name = models.CharField( verbose_name='last name', max_length=255, unique=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = [] # Email & Password are required by default.

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.username





# class CustomUserManager(BaseUserManager):
#     """
#         create & save users using username address and passwprd
#     """
#     def create_user(self, email, username, first_name, last_name, group, password, **extra_fields):
#         if not email:
#             raise ValueError('Your Email must be set')
#         if not username:
#             raise ValueError('Your Username must be set')
#         email = self.normalized_email(email)
#         user = self.model(
#             email=email,
#             usernam=username,
#             first_name=first_name,
#             last_name=last_name,
#             group=group
#             **extra_fields,
#             )
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, username, first_name, last_name, group, password, **extra_fields):
#         """
#             create & save users using username address and password
#         """
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True')
#         return self.create_user(email, username, first_name, last_name, group, password, **extra_fields)



# class CustomUserAdmin(UserAdmin, UpdateView):
#     add_form: CustomUserCreationForm
#     form = CustomUserChangeForm
#     # The forms to add and change user instances
#     model = CustomUser
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('username', 'first_name', 'last_name', 'is_staff', 'is_active','email')
#     list_filter = ('username',  'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser')
#     fieldsets = (
#         (None, {'fields': ('username', 'email', 'password')}),
#         ('Permissions',{'fields': ('is_staff',('is_active', 'is_superuser'), )}),
#         ('Important dates',{'fields': ('last_login','dates_joined')}),
#         ('Advanced options', {
#             'classes': ('collapse', ), 
#             'fields': ('groups', 'user_permissions'),
#         }),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups')}
#         ),
#     )
#     search_fields = ('username')
#     ordering = ('username',)