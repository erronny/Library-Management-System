from django.contrib.auth import get_user_model

User = get_user_model()


def user_count(request):
    return {'total_user': User.objects.filter(is_active=1).count()}
