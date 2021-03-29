# Generated by Django 3.1.7 on 2021-03-28 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='deliveries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'deliveries',
                'verbose_name_plural': 'deliveriess',
            },
        ),
        migrations.CreateModel(
            name='resultreq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ImageField(blank=True, default='default.png', upload_to='media')),
            ],
            options={
                'verbose_name': 'resultreq',
                'verbose_name_plural': 'resultreqs',
            },
        ),
        migrations.CreateModel(
            name='userfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('birthlocation', models.CharField(blank=True, max_length=25, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='violation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policenum', models.IntegerField()),
                ('carnum', models.IntegerField()),
                ('motornum', models.IntegerField()),
                ('cartype', models.CharField(max_length=30, null=True)),
                ('filenum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pishkhanapp.userfile')),
            ],
            options={
                'verbose_name': 'violation',
                'verbose_name_plural': 'violations',
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeofservice', models.CharField(blank=True, choices=[('DrivingLiscense', 'DrivingLiscense'), ('Passport', 'Passport'), ('SSCard', 'SSCard'), ('Violation', 'Violation')], max_length=25, null=True)),
                ('servicedate', models.DateField()),
                ('filenum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pishkhanapp.userfile')),
                ('result', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pishkhanapp.resultreq')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
        migrations.CreateModel(
            name='medicalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.ImageField(blank=True, default='default.png', upload_to='media')),
                ('filenum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pishkhanapp.userfile')),
            ],
            options={
                'verbose_name': 'medicalform',
                'verbose_name_plural': 'medicalforms',
            },
        ),
        migrations.CreateModel(
            name='files_archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perimage', models.ImageField(upload_to='media')),
                ('militimage', models.ImageField(upload_to='media')),
                ('medimage', models.ImageField(upload_to='media')),
                ('natimage', models.ImageField(upload_to='media')),
                ('filenum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pishkhanapp.userfile')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pishkhanapp.service')),
            ],
        ),
    ]
