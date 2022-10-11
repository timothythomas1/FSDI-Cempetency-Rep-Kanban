from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
        create & save users using username address and passwprd
    """
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError(_('Your Email must be set'))
        if not username:
            raise ValueError(_('Your Username must be set'))
        email = self.normalized_email(email)
        user = self.model(
            usernam=username,
            email=email
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
            create & save users using username address and passwprd
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
    