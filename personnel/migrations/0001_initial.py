# Generated by Django 4.2.3 on 2023-07-21 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('service_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('file_number', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('rank', models.CharField(max_length=10)),
            ],
        ),
    ]
