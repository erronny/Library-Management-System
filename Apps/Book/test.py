from django.contrib.auth import get_user_model

User = get_user_model()
queryset = User.objects.all()
print(queryset)
first_five = queryset[:5]
first_ten = queryset[:10]
