# Generated by Django 4.2.4 on 2024-09-16 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_details_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='image',
        ),
    ]
