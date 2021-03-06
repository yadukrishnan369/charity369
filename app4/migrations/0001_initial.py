# Generated by Django 3.2.8 on 2022-03-02 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app6', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='usersignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('useremail', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('address', models.SlugField(default='', max_length=100)),
                ('website', models.CharField(default='', max_length=100)),
                ('bio', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=50)),
                ('whatsapp', models.CharField(default='', max_length=50)),
                ('aboutme', models.SlugField(default='', max_length=1000)),
                ('picture', models.ImageField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='FoodDonation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodType', models.CharField(max_length=200)),
                ('foodQuantity', models.IntegerField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('address', models.SlugField(max_length=500)),
                ('buildingNumber', models.CharField(max_length=1000)),
                ('tradeMark', models.SlugField(max_length=500)),
                ('FoodRequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app6.foodrequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.usersignup')),
            ],
        ),
        migrations.CreateModel(
            name='EventsRegistrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app6.addevents')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.usersignup')),
            ],
        ),
    ]
