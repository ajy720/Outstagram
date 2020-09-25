import pdb

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from user.forms import UserForm

# Create your views here.
from user.models import User


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
            return redirect('post:main')
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

    if user_from in user_to.followers.all():
        user_from.following.remove(user_to)
        user_to.followers.remove(user_from)
        flag = False
    else:
        user_from.following.add(user_to)
        user_to.followers.add(user_from)
        flag = True

    user_from.save()
    user_to.save()

    data = {
        "flag": flag,
        "count": user_to.followers.count(),
    }

    return JsonResponse(data)