# Library-Management-System

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

