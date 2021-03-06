# Generated by Django 2.2.10 on 2020-07-09 04:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200709_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='mobile number should be in the format "+999999999" ', regex='^([+][0-9]{1,4}[6-9][0-9]{9})$')]),
        ),
    ]
