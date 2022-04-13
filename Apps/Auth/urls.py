from django.urls import path
from . import views

app_name = 'Auth'
urlpatterns = [
    path('admin/dashboard', views.index, name='dashboard'),
    path('admin/users/', views.user_list, name="users"),
    path('admin/create_user/', views.create_user, name="create_user"),
    path('admin/edit_user/<id>', views.edit_user, name="edit_user"),
    path('admin/view_user/<id>', views.view_user, name="view_user"),

    path('admin/group/', views.group_list, name="group"),
    path('admin/create_group/', views.create_group, name="create_group"),
    path('admin/edit_group/<id>', views.edit_group, name="edit_group"),
    path('admin/view_group/<id>', views.view_group, name="view_group"),

    path('admin/permission/', views.permission_list, name="permission"),
    path('admin/create_permission/', views.create_permission, name="create_permission"),
    path('admin/edit_permission/<id>', views.edit_permission, name="edit_permission"),
    path('admin/view_permission/<id>', views.view_permission, name="view_permission"),

    path('admin/profile_update/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('admin/profile/', views.ProfileView.as_view(), name='profile'),
    path('admin/change_password/', views.change_password, name='change_password'),
]