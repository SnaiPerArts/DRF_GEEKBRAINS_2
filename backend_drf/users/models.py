from django.db import models
from django.contrib.auth.models import AbstractUser

class UserInfo(AbstractUser):
    email = models.EmailField(unique=True)
    is_manage = models.BooleanField('Менеджер проекта', default=False)
    is_developer = models.BooleanField('Разработчик', default=False)