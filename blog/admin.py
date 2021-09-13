from django.contrib import admin
from .models import Category, CategoryAdmin, Comment, CommentAdmin, Post, PostAdmin, Contact, ContactAdmin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
