# Generated by Django 2.2.5 on 2019-10-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
