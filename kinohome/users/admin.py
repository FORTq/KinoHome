from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [field.name for field in CustomUser._meta.fields]

admin.site.register(CustomUser, CustomUserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileAdmin)

class FavoritesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Favorites._meta.fields]

    class Meta:
        model = Favorites


admin.site.register(Favorites, FavoritesAdmin)


class PlansAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Plans._meta.fields]

    class Meta:
        model = Plans


admin.site.register(Plans, PlansAdmin)



class EmailSubAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EmailSub._meta.fields]

    class Meta:
        model = EmailSub


admin.site.register(EmailSub, EmailSubAdmin)