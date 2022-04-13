from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm
from django.contrib.auth.hashers import make_password
from .models import *

User = get_user_model()


class RegisterForm(forms.ModelForm):
    """
    The default
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean_email(self):

        # Verify email is available.

        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        '''
        Verify both passwords match
        '''
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        if password is not None and password != password_2:
            self.add_error("password_2", "Your passwords must match")
        return cleaned_data


# class UserCreateForm(UserCreationForm):
class UserCreateForm(forms.ModelForm):
    """
    A form for creating new user. Includes all the required fields, plus a repeated password.
    """
    # password = forms.CharField(widget=forms.PasswordInput)
    # password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                               'id': 'first_name', 'name': 'first_name',
                                                               'value': "", 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                              'id': 'last_name', 'name': 'last_name',
                                                              'value': "", 'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'type': 'text',
                                                           'id': 'email', 'name': 'email',
                                                           'value': "", 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'text',
                                                                 'id': 'password', 'name': 'password',
                                                                 'value': "", 'class': 'form-control'}))
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'type': 'text',
                                                                                             'id': 'password_2',
                                                                                             'name': 'password_2',
                                                                                             'value': "",
                                                                                            'class': 'form-control'}))


    # password = make_password(unhasedpassword)

    CHOICES = (
        ("1", "Yes"),
        ("0", "No"),

    )
    is_superuser = forms.ChoiceField(choices=CHOICES)
    is_staff = forms.ChoiceField(choices=CHOICES)
    is_active = forms.ChoiceField(choices=CHOICES)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff')
        # exclude = ()

    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super(UserCreateForm, self).clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        is_active = cleaned_data.get("is_active")
        is_superuser = cleaned_data.get("is_superuser")
        is_staff = cleaned_data.get("is_staff")
        email = cleaned_data.get("email")

        if password is not None and password != password_2:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(UserCreateForm, self).save(commit=False)
    #     user.first_name('first_name')
    #     user.last_name('last_name')
    #     user.email('email')
    #     user.set_password(self.cleaned_data["password"])
    #
    #     if commit:
    #         # user = User.create_superuser()
    #         user.save()
    #     return user
    #
    # def __init__(self, *args, **kwargs):
    #     super(UserCreateForm, self).__init__(*args, **kwargs)


class UserEditForm(UserChangeForm):
    """A form for updating users. Includes all the fields on the user, but replaces the password
    field with admin's password hash display fields.
    """
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                               'id': 'first_name', 'name': 'first_name',
                                                               'value': "", 'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                              'id': 'last_name', 'name': 'last_name',
                                                              'value': "", 'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'type': 'text',
                                                           'id': 'email', 'name': 'email',
                                                           'value': "", 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'text',
                                                                 'id': 'password', 'name': 'password',
                                                                 'value': "",
                                                                 'class': 'form-control'}))
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'type': 'text',
                                                                                             'id': 'password_2',
                                                                                             'name': 'password_2',
                                                                                             'value': "",
                                                                                             'class': 'form-control'}))
    CHOICES = (
        ("1", "Yes"),
        ("0", "No"),

    )
    is_superuser = forms.ChoiceField(choices=CHOICES)
    is_staff = forms.ChoiceField(choices=CHOICES)
    is_active = forms.ChoiceField(choices=CHOICES)
    # password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff']
    def clean(self):
        '''
        Verify both passwords match.
        '''
        cleaned_data = super(UserEditForm, self).clean()
        password = cleaned_data.get("password")
        password_2 = cleaned_data.get("password_2")
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        is_active = cleaned_data.get("is_active")
        is_superuser = cleaned_data.get("is_superuser")
        is_staff = cleaned_data.get("is_staff")
        email = cleaned_data.get("email")

        if password is not None and password != password_2:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data
    def clean_password(self):
        """Regardless of what the user provides, return the initial value. This is done here, rather than on
         the field, because the field does not have access to the initial value"""
        return self.initial["password"]


class GroupForm(forms.ModelForm):
    """A form for creating group. Includes all the fields on the group
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'name', 'name': 'name',
                                                         'value': "", 'class': 'form-control'}))

    class Meta:
        model = Group
        fields = ['name']


class ChangeGroupForm(forms.ModelForm):
    """A form for creating group. Includes all the fields on the group
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'name', 'name': 'name',
                                                         'value': "", 'class': 'form-control'}))

    class Meta:
        model = Group
        fields = ['name']


class PermissionForm(forms.ModelForm):
    """A form for creating group. Includes all the fields on the group
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'name', 'name': 'name',
                                                         'value': "", 'class': 'form-control'}))
    content_type_id = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'content_type_id', 'name': 'content_type_id',
                                                         'value': "", 'class': 'form-control'}))
    codename = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'codename', 'name': 'codename',
                                                         'value': "", 'class': 'form-control'}))

    class Meta:
        model = Permission
        fields = ['name', 'content_type_id', 'codename']


class ChangePermissionForm(forms.ModelForm):
    """A form for creating group. Includes all the fields on the group
    """
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                         'id': 'name', 'name': 'name',
                                                         'value': "", 'class': 'form-control'}))
    content_type_id = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'text',
                                                                       'id': 'content_type_id',
                                                                       'name': 'content_type_id',
                                                                       'value': "", 'class': 'form-control'}))
    codename = forms.CharField(widget=forms.TextInput(attrs={'type': 'text',
                                                             'id': 'codename', 'name': 'codename',
                                                             'value': "", 'class': 'form-control'}))

    class Meta:
        model = Permission
        fields = ['name', 'content_type_id', 'codename']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [

            'first_name',
            'last_name',
            'email',
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'profile_image'

        ]


############################################################################

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)
