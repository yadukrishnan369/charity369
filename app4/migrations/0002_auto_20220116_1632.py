# Generated by Django 3.2.8 on 2022-01-16 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersignup',
            old_name='email',
            new_name='useremail',
        ),
        migrations.RenameField(
            model_name='usersignup',
            old_name='name',
            new_name='username',
        ),
    ]
