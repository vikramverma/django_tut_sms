# Generated by Django 2.2.5 on 2019-10-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191006_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fathers_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='husband_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
