from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Blog(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default='title')
    content = models.CharField(max_length=1000,default='content')

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment = models.CharField(max_length=200,default='comment')
