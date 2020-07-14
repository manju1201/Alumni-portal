# Generated by Django 2.2.10 on 2020-07-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200708_2124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='linkedin_id',
            new_name='github_url',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='webpage',
            new_name='linkedin_url',
        ),
        migrations.AddField(
            model_name='user',
            name='webpage_url',
            field=models.URLField(blank=True),
        ),
    ]
