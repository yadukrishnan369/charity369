# Generated by Django 3.2.8 on 2022-04-20 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0010_fooddonation_iscollected'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersignup',
            name='picture',
            field=models.ImageField(default='', upload_to='usersignup/'),
        ),
    ]
