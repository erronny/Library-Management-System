"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from Apps.Auth.views import HomeView
urlpatterns = [
    path('', auth_views.LoginView.as_view(
        template_name='admin/login.html',
        # authentication_form=LoginForm,
        extra_context={

            # option 1: provide full path
            'next': '/admin/dashboard/',

            # option 2: just provide the name of the url
            # 'next': 'custom_url_name',
        },
    ), name='login'),
    path('admin/', auth_views.LoginView.as_view(
        template_name='admin/login.html',
        # authentication_form=LoginForm,
        extra_context={

            # option 1: provide full path
            'next': '/admin/dashboard/',

            # option 2: just provide the name of the url
            # 'next': 'custom_url_name',
        },
    ), name='login'),
    # path('admin/', admin.site.urls, name='login'),
    # path('', HomeView.as_view(), name='home'),
    path('logout/', auth_views.LogoutView.as_view(
            next_page='login'
            ),
            name='logout'
        ),
    
    path('', include('Apps.Book.urls')),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

