from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from datetime import datetime, date


class UserQuerySet(models.QuerySet):
    def superuser(self):
        return self.filter(role='superuser')

    def staff(self):
        return self.filter(role='staff')


class UserManager(BaseUserManager):

    # def get_queryset(self):
    #     return UserQuerySet(self.model, using=self._db)

    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not first_name:
            raise ValueError("Users must have an first name")
        if not last_name:
            raise ValueError("Users must have an last name")
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, first_name, last_name):
        """
        Creates and save a staff user with the given email and password
        """
        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, first_name, last_name):
        """
        Creates and saves a superuser with the given email and password.
        """

        user = self.create_user(
            email,
            first_name,
            last_name,
            password=password,
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# class User(models.Model):
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, default=False, blank=False,
                              null=False)
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False)
    date_joined = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=True)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    # a superuser
    is_superuser = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(auto_now=True)

    # notice the absence of a "Password fields", that is built in.
    USERNAME_FIELD = 'email'
    # Email and password are required by default
    REQUIRED_FIELDS = ['first_name', 'last_name']
    # this is UserManager objects that inherit user manager of django through above code
    objects = UserManager()
    # .create_superuser(email, first_name, last_name)

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name, self.last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_username(self):
        return self.email

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"

        # Simplest possible answer: Yes, always
        return True

    def has_module_perm(self, app_label):
        "Does the user have permission to view the app 'app_label'?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staffuser(self):
        "Is the user a member of staff?"
        return self.is_staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.is_superuser

    @property
    def user_status(self):
        return self.is_active


class Group(models.Model):
    name = models.CharField(max_length=255, blank=False)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=255, blank=False)
    content_type_id = models.IntegerField(blank=False)
    codename = models.CharField(max_length=255, blank=False)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name, self.content_type_id, self.codename

userobj = User()

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(userobj, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()