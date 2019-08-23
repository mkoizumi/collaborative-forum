"""forum_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from forum_project import views


urlpatterns = [
    # sort of a default page
    url(r'^$', views.HomePage.as_view(), name = "home"),  # regex - no argument,just plain front page
    url(r'^admin/', admin.site.urls),
    # including inadividual app's url
    url(r'^account/', include("account.urls", namespace = "account")),
    url(r'^account/', include("django.contrib.auth.urls")),
    url(r'^complete/', views.LogoutPage.as_view(), name = "complete"),
    url(r'^post/', include("post.urls"), name = "post"),
    url(r'^topic/', include("topic.urls"), name = "topic"),

     # from here you can extend it to any regex in template app
]
