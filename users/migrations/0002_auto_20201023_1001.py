# Generated by Django 3.1.2 on 2020-10-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics', verbose_name='profile image'),
        ),
    ]
