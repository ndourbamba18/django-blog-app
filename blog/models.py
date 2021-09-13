from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f'{ self.name }'

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name="posts")

    def __str__(self):
        return f'{ self.title }'


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{ self.author }'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return f'{ self.name } Contact'



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','body', 'created_on', 'last_modified')
    list_filter = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'created_on', 'post')
    list_filter = ('author',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    list_filter = ('name',)

