# Generated by Django 4.2.1 on 2023-05-06 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asanpay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='is_error',
        ),
    ]