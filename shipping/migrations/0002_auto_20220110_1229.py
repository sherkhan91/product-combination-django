# Generated by Django 3.2.11 on 2022-01-10 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='created',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='modified',
        ),
    ]