from django.contrib import messages
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.views import generic
from topic.models import Topic, TopicMember
from . import models

class CreateTopic(LoginRequiredMixin, generic.CreateView):
    fields = ("name", "description")
    model = Topic

class SingleTopic(generic.DetailView):
    model = Topic

class ListTopics(generic.ListView):
    model = Topic


class JoinTopic(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("topic:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        topic = get_object_or_404(Topic,slug=self.kwargs.get("slug"))

        try:
            TopicMember.objects.create(user=self.request.user,topic=topic)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(topic.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(topic.name))

        return super().get(request, *args, **kwargs)


class LeaveTopic(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("topic:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.TopicMember.objects.filter(
                user=self.request.user,
                topic__slug=self.kwargs.get("slug")
            ).get()

        except models.TopicMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)
