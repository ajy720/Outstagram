from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, \
    PasswordChangeForm

User = get_user_model()


# UI와 데이터를 주고 받을 사용자 폼 양식
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields


# UI와 데이터를 주고 받을 회원정보 수정 폼 양식
class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("image", "username")


# UI와 데이터를 주고 받을 비밀번호 폼 양식
class PasswordEditForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")
