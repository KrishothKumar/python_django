# Generated by Django 2.2.3 on 2019-07-22 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_register', '0002_auto_20190721_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=4),
        ),
    ]
