# Generated by Django 4.1.3 on 2023-03-21 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profileing',
            new_name='profileimg',
        ),
    ]