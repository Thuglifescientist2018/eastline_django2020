from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL
# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    topic = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    write = models.TextField()