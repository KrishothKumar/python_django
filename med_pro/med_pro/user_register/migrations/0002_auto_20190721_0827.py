# Generated by Django 2.2.3 on 2019-07-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.TextField(max_length=1000),
        ),
    ]
