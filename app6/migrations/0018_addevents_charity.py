# Generated by Django 3.2.8 on 2022-02-25 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0017_remove_addevents_charity'),
    ]

    operations = [
        migrations.AddField(
            model_name='addevents',
            name='charity',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app6.charitysignup'),
        ),
    ]
