from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from user.forms import UserForm, UserEditForm, PasswordEditForm
# Create your views here.
from user.models import User, UserFollowing


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            # 현재 폼에는 이메일도 들어있음. forms.py에서 email을 추가해줬기 때문
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # authenticate에는 username과 password만 들어가면 되기 때문에 따로 추출해 전달
            login(request, user)
            return redirect('user:profile')
            # 회원가입 후 해당 계정으로 로그인 후 메인화면으로 이동
    else:
        form = UserForm()

    return render(request, 'user/signup.html', {'form': form})


@login_required(login_url="user:login")
def profile(request, id=None):
    if id:
        # 해당 ID를 가진 프로필
        profile = get_object_or_404(User, username=id)
        pass
    else:
        # 본인 프로필
        profile = User.objects.get(id=request.user.id)

    context = {
        'profile': profile,

    }

    return render(request, 'user/profile.html', context)


def follow(request, user_id):
    user_from = get_object_or_404(User, id=request.user.id)
    user_to = get_object_or_404(User, id=user_id)

    followers = [user.user_from for user in user_to.followers.all()]

    # pdb.set_trace()

    if user_from in followers:
        UserFollowing.objects.get(user_from=user_from, user_to=user_to).delete()
        flag = False
    else:
        UserFollowing.objects.create(user_from=user_from, user_to=user_to)
        flag = True

    data = {
        "flag": flag,
        "count": user_to.followers.count(),
    }

    return JsonResponse(data)


def edit(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            update_session_auth_hash(request, user)

            return redirect("user:profile")
    else:
        form = UserEditForm(instance=user)

    context = {
        "form": form,
    }

    return render(request, 'user/edit.html', context)


def password(request):
    user = get_object_or_404(User, id=request.user.id)

    if request.method == "POST":
        form = PasswordEditForm(user, request.POST)
        # PasswordChangeForm은 kwargs가 아닌 args로 (user, data) 순으로 받는다

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            update_session_auth_hash(request, user)

            return redirect("user:profile")
    else:
        form = PasswordEditForm(user)

    context = {
        "form": form,
    }

    return render(request, 'user/password.html', context)
