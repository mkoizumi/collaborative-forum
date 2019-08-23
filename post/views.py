from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic  # taking advantage of already defined generic view
from django.http import Http404
from post import models
from post import models

from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ('user', 'topic')

class UserPosts(generic.ListView):
    model = models.Post
    template_name = "post/post_list.html"

    # check for user existance
    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("post").get(username__iexact=self.kwargs.get("username"))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.post.all()

    # connected to specific user who posted
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context


class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ("user", "topic")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get("username"))


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # form_class = forms.PostForm
    fields = ('message','topic')
    model = models.Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = models.Post
    select_related = ("user", "topic")
    success_url = reverse_lazy("post:all")  # take you back to post list

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
