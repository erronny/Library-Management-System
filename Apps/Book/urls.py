from django.urls import path
from . import views

app_name = 'Book'
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