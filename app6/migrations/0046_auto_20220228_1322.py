# Generated by Django 3.2.8 on 2022-02-28 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0016_alter_userreg_email'),
        ('app6', '0045_auto_20220228_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsregistrations',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app6.addevents'),
        ),
        migrations.AlterField(
            model_name='eventsregistrations',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app4.usersignup'),
        ),
    ]