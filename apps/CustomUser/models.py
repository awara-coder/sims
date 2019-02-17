from django.db import models
from django.contrib.auth.models import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    fullname = models.CharField(max_length = 100)
    address = models.TextField()
    username = models.CharField(max_length = 200)
    CATEGORY_CHOICES = (
    	('IN', 'Investor'),
    	('ME', 'Mentor'),
    	('FO', 'Founder'),
    	)
    category = models.CharField(max_length = 2, choices = CATEGORY_CHOICES, default = 'IN')
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    ACTIVATED_CHOICES = (
        ('YES', 'Verified'),
        ('NO', 'Not Verified'),
        )
    is_activated = models.CharField(
        max_length= 3,
    	default = 'NO',
        choices= ACTIVATED_CHOICES,
    	help_text = _(
    		'Designates whether this user is verified by ' 
    		'the moderator(admin)')
    	),
    phoneno = PhoneNumberField(null = True, blank = True)
    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email