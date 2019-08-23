from django.db import models
from django.urls import reverse
from django.conf import settings
from topic.models import Topic
from django.contrib.auth import get_user_model

# user mark down within their post
import misaka

# Create your models here.
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name = "post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now = True) # gives the time
    message = models.TextField()
    message_html = models.TextField(editable = False)
    topic = models.ForeignKey(Topic, related_name = "post", null = True, blank = True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:single', kwargs = {"username":self.user.username, "pk":self.pk})

    class Meta:
        ordering = ['-created_at'] # most recent at the top
        unique_together = ["user", "message"]
