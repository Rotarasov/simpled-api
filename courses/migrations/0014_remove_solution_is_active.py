# Generated by Django 3.1.2 on 2020-12-16 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20201209_1454'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solution',
            name='is_active',
        ),
    ]