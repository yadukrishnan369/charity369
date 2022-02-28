# Generated by Django 3.2.8 on 2022-02-28 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0015_alter_userreg_email'),
        ('app6', '0044_auto_20220228_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addevents',
            name='charity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app6.charitysignup'),
        ),
        migrations.AlterField(
            model_name='eventsregistrations',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app6.addevents'),
        ),
        migrations.AlterField(
            model_name='eventsregistrations',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.usersignup'),
        ),
    ]