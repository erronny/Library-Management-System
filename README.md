# Library-Management-System
### OverView
1. Version
2. Database
3. Migrate & Operations
4. 


### Versions 
Python - 3.8.10 \
Django - 2.2.6


Download and extract the zip file. Try ```python3 manage.py runserver``` If server not started or if you wanted to perform migrations operations follow these steps:-

### Database
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Your_database_name',
        'USER': 'Your_User_name',
        'PASSWORD': 'Your_User_Password',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
```
put your mysql details as like above. If you didn't want to use MySql then comment this lines and uncomment bellow lines.
```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
```
Uncomment these lines to use DBSqLite.
I Have uploaded database file also if not works use them in worst case secanerio.

### Migrate & Operations
Make migrations of Auth app for Auth database table
```python3 manage.py makemigrations Auth```


<b>Output</b>
```
Migrations for 'Auth':
  Apps/Auth/migrations/0001_initial.py
    - Create model Group
    - Create model Permission
    - Create model User
    - Create model Profile
```
Make migrations of Book App for Book database table
```python3 manage.py makemigrations Book```

<b>Output</b>
```
Migrations for 'Book':
  Apps/Book/migrations/0001_initial.py
    - Create model Book
```
Now Migrate
```python3 manage.py migrate```
<b>Output</b>

```
Operations to perform:
  Apply all migrations: Auth, Book, admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying Auth.0001_initial... OK
  Applying Book.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying sessions.0001_initial... OK
  ```





### Book Module/app segment
Here we are going to write some code to work on database. Here we considering 5 main details of books. i.e Title, summary, Author, Book Code and No Of book available. Some other fields are required for django system and for making things easy. i.e id field is not mandatory it'll created automatically.

Status(Boolean):- We will show only active book so we are using status ```True``` by-default.
is_deleted(Boolean) : - We are going to to use soft delete concept here it stores ```False``` by-default, when delete operation performed book never be deleted, it will change into ```True``` As like Trash Bin.
created_at:- This is DateTime fields that stores when book is created.
updated_at:- This is also an DateTime fields that store when last time book is updated.


```
from django.db import models
import datetime


class Book(models.Model):
    id = models.AutoField(primary_key=True)    
    title = models.CharField(max_length=100, verbose_name="First Name") 
    summary = models.TextField(max_length=255, verbose_name="summary")
    author = models.TextField(max_length=255, verbose_name="Author")
    book_code = models.CharField(max_length=255, unique=True, verbose_name="Book Code")
    no_of_book = models.IntegerField()   
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=datetime.date.today)
    updated_at = models.DateField(auto_now=True)
```
It is an instance method when we search or call for Book Module from anywhere, this function returns their title. We can return Book Code or and author as well.
```

    def __str__(self):
        return self.title
```


Below we importing render function Http Response function to except route hits, when route hits by user this function response on behalf of type of requests. We also importing login required decorator from auth. Django have built-in decorator we are using them for validation, When any user try to acess that view function these function rejects the request and return error response, OR redirect to login and sign up page. Decorator is an sepcial kind of function that add some special and common functionlity in existing function. It's like decorating christmas tree, tree is an existing function and decorated things are decorator function. 

```
from django.shortcuts import render
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .forms import *


```

#### Showing all book data and passing in table
```
# Employee
@login_required
def book_list(request):
    context = {}
    context['dataset'] = Book.objects.filter(is_deleted=False)
    context['trash'] = Book.objects.filter(is_deleted=True)
    return render(request, 'admin/Book/list.html', context)

```
```context = {}``` this is an dictionary named with context
```context['dataset'] = Book.objects.filter(is_deleted=False)``` we are storing book by filtering if Book is not deleted then store in context key is dataset.
```context['trash'] = Book.objects.filter(is_deleted=True)``` We are storing deleted data by filtering if book is deleted then store in context key is trash.

#### Enabling the status of Book
Below view is to enable disabled book by status. basically we changing the status of book.
```
@login_required
def enable_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.status = True
    data_obj.save(update_fields=["status"])
    return HttpResponseRedirect("/"'admin'"/"'book')

```
``` data_obj = Book.objects.get(id=id)``` data_obj is an variable that stores book by their id then we changing the status column by setting `True`
Finally we using save function to perform changes operations on databases.



#### Disabling the status of Book
Below view is to disable enabled book by status. basically we changing the status of book.
```
@login_required
def disable_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.status = False
    data_obj.save(update_fields=["status"])
    return HttpResponseRedirect("/"'admin'"/"'book')

```
``` data_obj = Book.objects.get(id=id)``` data_obj is an variable that stores book by their id then we changing the status column by setting `False` ```data_obj.status = False```

```data_obj.save(update_fields=["status"])``` Finally we using save function to perform changes operations on databases.



#### Performing Soft Delete
Here we deleting book or data from book table logically, but it will never get deleted, it only change the `True` means it perform operation on `is_deleted` column then set `True` So when we fetch the data from table it will show only data with `is_deleted` with `False` Value.

```
@login_required
def trash_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.is_deleted = True
    data_obj.save(update_fields=["is_deleted"])
    return HttpResponseRedirect("/"'admin'"/"'book')
```




#### Restoring Book
Here we Reversing the `is_deleted` column value to 'False`. Means we can restore deleted data from column\
`data_obj.is_deleted = False` this lines shows we changing the value `False` From `True`
```
@login_required
def restore_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.is_deleted = False
    data_obj.save(update_fields=["is_deleted"])
    return HttpResponseRedirect("/"'admin'"/"'book')
```


#### Deleting Book
Finally we Deleting the book from database for permanently, we using hard delete operation and using `delete()` function

```
@login_required
def delete_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.delete()
    return HttpResponseRedirect("/"'admin'"/"'book')
```


#### Adding Book
We adding Book here, like we using `POST` method to get data from `form` named `BookForm`, calling cleaned_data from django form storing in a variables named data, then accessing them by indexing method using name.

```
@login_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST or None)
        if form.is_valid():
            data = form.cleaned_data
            
            title = data['title']
            author = data['author']            
            book_code = data['book_code']
            no_of_book = data['no_of_book']           
            summary = data['summary']
           
            status = True
            # user = request.user.id
            is_deleted = False
            book = Book(title=title,
                                author=author,
                                book_code=book_code,
                                no_of_book=no_of_book,
                                summary=summary,                                
                                status=status,                                
                                is_deleted=is_deleted)
            
            book.save()
            return HttpResponseRedirect("/"'admin'"/"'book')
        else:
            print(form.errors)
    else:
        form = BookForm()
    return render(request, 'admin/Book/add.html', {'form': form})
```
We already stored all upcoming data from `BookForm` now we passing all variables `Book()` inside Model by importing, and storing in a variables named `book`. Then saving them using `save()` function. save function run mysql quries to make changes in database.



#### Changing Existing book
Also we doing same things we doing in `add_book` view, the changes is, we loading specific data by using their id and passing them in `BookForm` to display using `GET` method then we using post method to store same or updated data coming from `BookForm`.
```
@login_required
def change_book(request, id):
    data_obj = Book.objects.get(id=id)
    form = BookForm(instance=data_obj)
    if request.method == 'POST':
        form = BookForm(data=request.POST, instance=data_obj)
        if form.is_valid():
            data = form.cleaned_data
            title = data['title']
            author = data['author']            
            book_code = data['book_code']
            no_of_book = data['no_of_book']           
            summary = data['summary']
            status = data_obj.status
            # user = request.user.id
            is_deleted = data_obj.is_deleted
            created_at = data_obj.created_at

            book = Book(id=id,
                                title=title,
                                author=author,
                                book_code=book_code,
                                no_of_book=no_of_book,
                                summary=summary,                                
                                status=status,                                
                                is_deleted=is_deleted)

            book.save()
            return HttpResponseRedirect("/"'admin'"/"'book')
        else:
            print(form.errors)
    return render(request, 'admin/Book/change.html', {'form': form})

```


#### View Book

It's simple we accessing data by using specific `id`. storing them in a dictionary named context.
```
@login_required
def view_book(request, id):
    context = {}
    context["data"] = Book.objects.get(id=id)
    return render(request, 'admin/Book/view.html', context)


#####################################
```
#### BookForm
```
class BookForm(forms.ModelForm):

   
    title = forms.CharField(label="First Name", required=True, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control'}))
    author = forms.CharField(label="Author", required=False, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control'}))
    
    
    book_code = forms.CharField(label="Book Code", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    no_of_book = forms.CharField(label="Joining Date", required=True, widget=forms.TextInput(
        attrs={'type': 'text', 'class': 'form-control'}))   
    summary = forms.CharField(label="Author", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control'}))
   

    class Meta:
        model = Book
        fields = ['title', 'author', 'book_code', 'no_of_book', 'summary']

    def clean(self):
        cleaned_data = super(BookForm, self).clean()
        title = cleaned_data.get("title")
        author = cleaned_data.get("author")
        book_code = cleaned_data.get("book_code")
        no_of_book = cleaned_data.get("no_of_book")
        summary = cleaned_data.get("summary")
        
        return cleaned_data
```
We creating a django form containg with relative fields what ia need. `widget=forms.TextInput()` Using widgets and html classes to makes them responsible no need to redesign and recode for frontend. We using `Meta` class. Basically it is key to tells model how many of fields are going to be changed or how many columns needed for updation.
Finally we using a function `Clean` using Oops concept of inheritance to inheriting the coming data using `super()` into fields and storing into variables and returning them.
#### Urls 
```
urlpatterns = [


    path('admin/book/', views.book_list, name="book"),
    path('admin/create_book/', views.add_book, name="create_book"),
    path('admin/change_book/<id>', views.change_book, name="change_book"),
    path('admin/view_book/<id>', views.view_book, name="view_book"),
    path('admin/enable_book/<id>', views.enable_book, name="enable_book"),
    path('admin/disable_book/<id>', views.disable_book, name="disable_book"),
    path('admin/trash_book/<id>', views.trash_book, name="trash_book"),
    path('admin/restore_book/<id>', views.restore_book, name="restore_book"),
    path('admin/delete_book/<id>', views.delete_book, name="delete_book"),

    ]
    ```
    These Above codes are url pattern making custom path and calling `view function` from `view page`. Naming the every path with different name beacuse we would be able to call them in frontend eaaly.

### Auth Module/app segment
#### Groups and Roles
We recoding the group or roles of django built-in roles function. Because we want more features and more controls over users. Finally `str()` function returns the group name. We are not going to use it right now but we can use it in future.
```
lass Group(models.Model):
    name = models.CharField(max_length=255, blank=False)
    status = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateField(default=date.today)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
 ```
#### Permisssions
Thsis is the permission table we also going to use i'll explain it later.
```
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
```

#### Filtering user by superuser and staff roles, UserQuerySet class inherited by django QuerySet that use function for filtering user as per our need, we using two roles type only.
```
class UserQuerySet(models.QuerySet):
    def superuser(self):
        return self.filter(role='superuser')

    def staff(self):
        return self.filter(role='staff')
```
#### UserManager
We defining some advance code for managing users creation and updation, when we hit `Class User` Model to create user this class will be called and manages as per need and django architechure. Here we changing User name with email, When you hit `python3 manage.py createsuperuser`. Django will ask you email, first_name, last_name and Easy password. In Default version of django django asked you for username and a complicated password, here we used inheritance concept to modify the Internal UserManager Class.
```
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

```
#### class UserModel
Here we creating User class to create database and storing users in db. Some of the required fields are and some of customs fields. Here we defined some of mandatory function like `has_perm`, `has_module_perm` and some of function to get the users data as like `first_name`, `last_name` `email` and `str()` function returns fullname.
```
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
 ```
 
 #### User View Functions
 
 ```
 # import datetime
from datetime import datetime, date, timedelta
from django.http import HttpResponse
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password

from Apps.Book.models import Book
from django.utils import timezone

# relative import of forms
from .models import Group, Permission, UserManager
from .forms import RegisterForm, UserCreateForm, UserEditForm, UserForm, ProfileForm, GroupForm, ChangeGroupForm, \
    PermissionForm, ChangePermissionForm
from django.contrib.auth import get_user_model

User = get_user_model()


```
#### Dashboard
```


def index(request):
    # Filter messages with specified Date and Time
    today_date = datetime.today().date
    today_month = datetime.today().month
    today_year = datetime.today().year
    today = date.today().strftime("%Y-%m-%d")
    first_date_of_month = datetime.today().replace(day=1).strftime('%Y-%m-%d')
    first_date_of_year = date(date.today().year, 1, 1).strftime('%Y-%m-%d')

    date_str = today
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    first_date_of_week = date_obj - timedelta(days=date_obj.weekday())

   
    # today data
    count_user_today = User.objects.filter(is_active=1, status=True, is_deleted=False, created_at__gte=today).count()
    count_book_today = Book.objects.filter(status=True, is_deleted=False, created_at__gte=today).count()
    # this week
    count_user_this_week = User.objects.filter(is_active=1, status=True, is_deleted=False,
                                               created_at__range=[first_date_of_week, today]).count()
    count_book_this_week = Book.objects.filter(status=True, is_deleted=False,
                                                       created_at__range=[first_date_of_week, today]).count()
     # this month data
    count_user_this_month = User.objects.filter(is_active=1, status=True, is_deleted=False,
                                                created_at__range=[first_date_of_month, today]).count()
    count_book_this_month = Book.objects.filter(status=True, is_deleted=False,
                                                        created_at__range=[first_date_of_month, today]).count()
    # this year data
    count_user_this_year = User.objects.filter(is_active=1, status=True, is_deleted=False,
                                               created_at__range=[first_date_of_year, today]).count()
    count_book_this_year = Book.objects.filter(status=True, is_deleted=False,
                                                       created_at__range=[first_date_of_year, today]).count()
    today_dataset = User.objects.filter(is_active=1, status=True, is_deleted=False, created_at__gte=today)
    this_week_dataset = User.objects.filter(is_active=1, status=True, is_deleted=False,
                                            created_at__range=[first_date_of_week, today])
    this_month_dataset = User.objects.filter(is_active=1, status=True, is_deleted=False,
                                             created_at__range=[first_date_of_month, today])
    this_year_dataset = User.objects.filter(is_active=1, status=True, is_deleted=False,
                                            created_at__range=[first_date_of_year, today])
    user_context = {'today_dataset': today_dataset, 'this_week_dataset': this_week_dataset,
                    'this_month_dataset': this_month_dataset, 'this_year_dataset': this_year_dataset}

    context = {'count_user_today': count_user_today, 'count_book_today': count_book_today,
               
               'count_user_this_week': count_user_this_week, 'count_book_this_week': count_book_this_week,
               
               'count_user_this_month': count_user_this_month, 'count_book_this_month': count_book_this_month,
               
               'count_user_this_year': count_user_this_year, 'count_book_this_year': count_book_this_year
               
               }
    return render(request, 'admin/index.html', context, user_context)

```
#### User_List
```
@login_required
def user_list(request):
    # dictionary for initial data with field name as keys
    context = {}
    context["dataset"] = User.objects.all()
    return render(request, "admin/User/list.html", context)

```
#### Create User
```
@login_required
def create_user(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = UserCreateForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        password = make_password(form.cleaned_data['password'])
        email = form.cleaned_data['email']
        is_active = form.cleaned_data['is_active']
        is_superuser = form.cleaned_data['is_superuser']
        is_staff = form.cleaned_data['is_staff']

        user = User(first_name=first_name, last_name=last_name, password=password, email=email,
                    is_active=is_active, is_superuser=is_superuser, is_staff=is_staff)
        user.save()

        return HttpResponseRedirect("/"'admin'"/"'users')
    # else:
    #     print("Something is wrong")
    context['form'] = form
    return render(request, "admin/User/create.html", context)
```
#### Edit User
```

@login_required
def edit_user(request, id):
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(User, id=id)

    # pass the object as instance in form
    form = UserEditForm(request.POST or None, instance=obj)

    # save the data from the form and redirect to view
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        password = make_password(form.cleaned_data['password'])
        email = form.cleaned_data['email']
        is_active = form.cleaned_data['is_active']
        is_superuser = form.cleaned_data['is_superuser']
        is_staff = form.cleaned_data['is_staff']

        user = User(first_name=first_name, last_name=last_name, password=password, email=email,
                    is_active=is_active, is_superuser=is_superuser, is_staff=is_staff)
        user.save()
        # form.save()
        return HttpResponseRedirect("/"'admin'"/"'users')

    # add form dictionary to context
    context["form"] = form
    return render(request, "admin/User/edit.html", context)

```
#### View User
```
@login_required
def view_user(request, id):
    context = {}

    context["data"] = User.objects.get(id=id)
    return render(request, "admin/User/view.html", context)


```
#### Group List
```
# Group code
@login_required
def group_list(request):
    # dictionary for initial data with field name as keys
    context = {}
    context["dataset"] = Group.objects.all()
    return render(request, "admin/Group/list.html", context)

```
#### Create Group
```
@login_required
def create_group(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"'admin'"/"'group')
    context['form'] = form
    return render(request, "admin/Group/add.html", context)

```
#### Edit Group
```
@login_required
def edit_group(request, id):
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Group, id=id)

    # pass the object as instance in form
    form = ChangeGroupForm(request.POST or None, instance=obj)

    # save the data from the form and redirect to view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"'admin'"/"'group')

    # add form dictionary to context
    context["form"] = form
    return render(request, "admin/Group/change.html", context)

```
#### View Group
```
@login_required
def view_group(request, id):
    context = {}

    context["data"] = Group.objects.get(id=id)
    return render(request, "admin/Group/view.html", context)

```

#Permission list
```
# Group code
@login_required
def permission_list(request):
    # dictionary for initial data with field name as keys
    context = {}
    context["dataset"] = Permission.objects.all()
    return render(request, "admin/Permission/list.html", context)
```
#### Create PErmission
```

@login_required
def create_permission(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = PermissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"'admin'"/"'group')
    context['form'] = form
    return render(request, "admin/Permission/add.html", context)

```
#### Edit Permission
```
@login_required
def edit_permission(request, id):
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Group, id=id)

    # pass the object as instance in form
    form = ChangePermissionForm(request.POST or None, instance=obj)

    # save the data from the form and redirect to view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"'admin'"/"'group')

    # add form dictionary to context
    context["form"] = form
    return render(request, "admin/Permission/change.html", context)

```
#### View Permission
```
@login_required
def view_permission(request, id):
    context = {}

    context["data"] = Permission.objects.get(id=id)
    return render(request, "admin/Permission/view.html", context)

```
#### Change Password
```

@login_required
def change_password(request):
    return render(request, "admin/User/change_password.html")


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy


```
#### Profile Updation

```
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'admin/User/profile_update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.Profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request)
```
#### Signup
```
```


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('admin/users')
    else:
        form = SignUpForm()
    return render(request, 'admin/User/create.html', {'form': form})
```
<img src="https://github-readme-stats.vercel.app/api/top-langs?username=erronny"/>
<img src="https://github-readme-stats.vercel.app/api/top-langs?username=erronny&layout=compact"/>
![GitHub stats](https://github-readme-stats.vercel.app/api?username=erronny&show_icons=true&theme=tokyonight)
