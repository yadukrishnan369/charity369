# Generated by Django 3.2.8 on 2022-02-28 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0036_alter_eventsregistrations_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsregistrations',
            name='event',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app6.addevents'),
        ),
        migrations.AlterField(
            model_name='eventsregistrations',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app6.charitysignup'),
        ),
    ]