# Generated by Django 4.1.3 on 2022-12-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstNameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='LastNameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
