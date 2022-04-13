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

    def __str__(self):
        return self.title


