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
