from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields


class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("image", "username",)
