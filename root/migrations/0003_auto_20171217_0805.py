# Generated by Django 2.0 on 2017-12-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_auto_20171217_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='using_setting',
            field=models.CharField(default='', max_length=100),
        ),
    ]
