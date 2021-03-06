# Generated by Django 3.2.9 on 2021-11-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookedcalls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='advisorid',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
