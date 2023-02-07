from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self):
        return self.username


# class QuesModel(models.Model):
#     question = models.CharField(max_length=200, null=True)
#     op1 = models.CharField(max_length=200, null=True)
#     op2 = models.CharField(max_length=200, null=True)
#     op3 = models.CharField(max_length=200, null=True)
#     op4 = models.CharField(max_length=200, null=True)
#     ans = models.CharField(max_length=200, null=True)
#
#     def __str__(self):
#         return self.question


class QuizModel(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200, null=False)
    image = models.ImageField(
        upload_to='images/',
        default='images\graphic-3373066_640.png',
    )

    def __str__(self):
        return self.title
