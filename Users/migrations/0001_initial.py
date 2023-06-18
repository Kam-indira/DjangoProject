# Generated by Django 4.1.3 on 2023-06-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=30)),
                ('occupation', models.CharField(max_length=30)),
                ('describeYourself', models.CharField(max_length=300)),
            ],
        ),
    ]
