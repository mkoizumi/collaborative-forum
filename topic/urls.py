from django.urls import path
from . import views

app_name = 'topic'

urlpatterns = [
    path('', views.ListTopics.as_view(), name="all"),
    path("new/", views.CreateTopic.as_view(), name="create"),
    path("posts/in/<slug>/",views.SingleTopic.as_view(),name="single"),
    path("join/<slug>/",views.JoinTopic.as_view(),name="join"),
    path("leave/<slug>/",views.LeaveTopic.as_view(),name="leave"),
]
