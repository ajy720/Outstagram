from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user.forms import UserForm

# Create your views here.
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

    return render(request, 'user/signup.html', {'form':form})