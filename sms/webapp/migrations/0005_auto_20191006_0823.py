# Generated by Django 2.2.5 on 2019-10-06 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20191006_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='fisrt_name',
            new_name='first_name',
        ),
    ]
