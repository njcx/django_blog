# Create your models here.
from django.db import models
from .base import BaseModel

class User(models.Model):
    name = models.CharField(max_length=30)
    qq = models.CharField(max_length=30)
    wechat = models.CharField(max_length=30)
    desc = models.TextField()
    email = models.EmailField()
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Blog(BaseModel):
    article_name = models.CharField(max_length=100)
    content = models.TextField()
    release =models.BooleanField()

    def __unicode__(self):
        return self.article_name

class Comment(BaseModel):
    user_name = models.CharField(max_length=100)
    qq = models.IntegerField()
    wechat = models.CharField(max_length=20)
    content = models.TextField()

    def __unicode__(self):
        return self.user_name

class Message(BaseModel):
    user_name = models.CharField(max_length=100)
    qq = models.IntegerField()
    wechat = models.CharField(max_length=20)
    content = models.TextField()
    phone = models.IntegerField()
    email = models.EmailField()
    ip = models.GenericIPAddressField()

    def __unicode__(self):
        return self.user_name

class SiteDesc(models.Model):
    site_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    kw = models.CharField(max_length=200)

    def __unicode__(self):
        return self.site_name