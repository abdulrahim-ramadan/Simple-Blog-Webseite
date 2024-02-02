from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=30000)
    image = models.ImageField(upload_to='posts')
    publish_date = models.DateTimeField(default=timezone.now)
    tags = TaggableManager()


class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comment_author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comment_post',on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    create_at = models.DateTimeField(default=timezone.now)






