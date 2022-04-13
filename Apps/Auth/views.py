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


class HomeView(TemplateView):
    template_name = 'admin/base_site.html'


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


@login_required
def user_list(request):
    # dictionary for initial data with field name as keys
    context = {}
    context["dataset"] = User.objects.all()
    return render(request, "admin/User/list.html", context)


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


@login_required
def view_user(request, id):
    context = {}

    context["data"] = User.objects.get(id=id)
    return render(request, "admin/User/view.html", context)


############################################
# Group code
@login_required
def group_list(request):
    # dictionary for initial data with field name as keys
    context = {}
    context["dataset"] = Group.objects.all()
    return render(request, "admin/Group/list.html", context)


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


@login_required
def view_group(request, id):
    context = {}

    context["data"] = Group.objects.get(id=id)
    return render(request, "admin/Group/view.html", context)


############################################
# Group code
@login_required
def permission_list(request):
    # dictionary for initial data with field name as keys
    context = {}
    context["dataset"] = Permission.objects.all()
    return render(request, "admin/Permission/list.html", context)


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


@login_required
def view_permission(request, id):
    context = {}

    context["data"] = Permission.objects.get(id=id)
    return render(request, "admin/Permission/view.html", context)


##########################################

@login_required
def change_password(request):
    return render(request, "admin/User/change_password.html")


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/User/profile.html'


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


#####################################################################
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
