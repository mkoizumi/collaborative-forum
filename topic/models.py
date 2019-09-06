from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.conf import settings
from django.urls import reverse

# Create your models here.

# need to install misaka - use command line install 
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# fields for topics
class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True) # generates valid URL
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User,through="TopicMember")
    
    def __str__(self):
        return self.name

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("topics:single", kwargs={"slug": self.slug})


    class Meta:
        ordering = ["name"]


class TopicMember(models.Model):
    topic = models.ForeignKey(Topic,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_topics',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("topic", "user")



