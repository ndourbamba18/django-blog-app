# Generated by Django 3.1.4 on 2021-04-30 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='image_pics'),
        ),
    ]
