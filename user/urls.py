from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, profile, follow, edit

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', signup, name="signup"),
    path('profile/', profile, name="profile"),
    path('profile/<str:id>', profile, name="profile"),
    path('follow/<int:user_id>', follow, name="follow"),
    path('edit/', edit, name="edit")

]