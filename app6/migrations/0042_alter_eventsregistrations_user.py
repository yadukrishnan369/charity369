# Generated by Django 3.2.8 on 2022-02-28 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0014_delete_eventsregistrations'),
        ('app6', '0041_eventsregistrations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsregistrations',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app4.usersignup'),
        ),
    ]