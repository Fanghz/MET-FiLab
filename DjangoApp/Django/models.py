from django.db import models as m

# Create your models here.

class Post(m.Model):
     content = m.CharField(max_length=256)
     created_at = m.DateTimeField('create date')

class Comment(m.Model):
    post = m.ForeignKey(Post)
    message = m.TextField()
    created_at = m.DateTimeField('create date')

class Register(m.Model):
    username = m.CharField(max_length=256)
    password = m.CharField(max_length=256)
    created_at = m.DateTimeField('created date')


