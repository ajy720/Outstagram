from django.contrib import admin

from .models import User, UserFollowing


# Register your models here.

@admin.register(UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ("id", "user_from", "user_to")


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username",)
