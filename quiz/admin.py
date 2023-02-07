from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, QuizModel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'is_staff', ]


class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(QuizModel, QuizAdmin)

