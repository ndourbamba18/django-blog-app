from django.db import models
from django.contrib import admin
from PIL import Image

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(default="default.jpg", upload_to="image_pics")

    def __str__(self):
        return f'{ self.title } Project'


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technology', 'image')
    list_filter = ('title',)
