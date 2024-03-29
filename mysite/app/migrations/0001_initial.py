# Generated by Django 4.0 on 2021-12-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('car_name', models.CharField(max_length=64, unique=True)),
                ('image', models.ImageField(upload_to='media/images')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
