# Generated by Django 3.2.8 on 2022-03-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0007_fooddonation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingdonation',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='medicinedonation',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='otherdonation',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='studymaterialdonation',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
