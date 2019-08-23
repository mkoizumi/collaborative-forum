from django.conf.urls import url
from django.contrib.auth import views as auth_views
from account import views

app_name = "account"

urlpatterns = [
    url(r'login/$', auth_views.LoginView.as_view(
            template_name = "account/login.html"), name = "login"),
    url(r'logout/$', auth_views.LogoutView.as_view(), name = "logout"),
    url(r'register/$', views.Register.as_view(), name = "register"),
]
