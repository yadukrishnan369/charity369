# Generated by Django 3.2.8 on 2022-03-02 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooddonation',
            name='FoodRequest',
        ),
    ]
