# Generated by Django 3.1.2 on 2020-12-17 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_remove_solution_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participation',
            name='is_active',
        ),
    ]
