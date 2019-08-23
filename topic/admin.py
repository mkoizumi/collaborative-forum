from django.contrib import admin
from topic import models

# Register your models here.
class TopicMemberInline(admin.TabularInline):
    model = models.TopicMember

admin.site.register(models.Topic)
