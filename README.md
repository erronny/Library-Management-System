# Library-Management-System
### OverView
1. Version
2. 


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
```

    def __str__(self):
        return self.title
```


```
from django.shortcuts import render
from django.shortcuts import (get_object_or_404, render, HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from .forms import *


```
```


#########################################################
# Employee
@login_required
def book_list(request):
    context = {}
    context['dataset'] = Book.objects.filter(is_deleted=False)
    context['trash'] = Book.objects.filter(is_deleted=True)
    return render(request, 'admin/Book/list.html', context)

```
```
@login_required
def enable_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.status = True
    data_obj.save(update_fields=["status"])
    return HttpResponseRedirect("/"'admin'"/"'book')

```
```
@login_required
def disable_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.status = False
    data_obj.save(update_fields=["status"])
    return HttpResponseRedirect("/"'admin'"/"'book')

```
```
@login_required
def trash_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.is_deleted = True
    data_obj.save(update_fields=["is_deleted"])
    return HttpResponseRedirect("/"'admin'"/"'book')
```
```

@login_required
def restore_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.is_deleted = False
    data_obj.save(update_fields=["is_deleted"])
    return HttpResponseRedirect("/"'admin'"/"'book')
```
```

@login_required
def delete_book(request, id):
    # fetch the object related to passed id
    data_obj = Book.objects.get(id=id)
    data_obj.delete()
    return HttpResponseRedirect("/"'admin'"/"'book')
```
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


```
@login_required
def view_book(request, id):
    context = {}
    context["data"] = Book.objects.get(id=id)
    return render(request, 'admin/Book/view.html', context)


#####################################
```

