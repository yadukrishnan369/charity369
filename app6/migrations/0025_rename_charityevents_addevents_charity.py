# Generated by Django 3.2.8 on 2022-02-25 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app6', '0024_alter_addevents_charityevents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addevents',
            old_name='charityevents',
            new_name='charity',
        ),
    ]
