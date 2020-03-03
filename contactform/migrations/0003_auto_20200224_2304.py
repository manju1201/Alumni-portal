# Generated by Django 2.2.9 on 2020-02-24 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0002_auto_20200224_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform_queries',
            name='replyform',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='contactform.ReplyForm_queries'),
        ),
        migrations.AlterField(
            model_name='replyform_queries',
            name='contactform',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='contactform.ContactForm_queries'),
        ),
    ]