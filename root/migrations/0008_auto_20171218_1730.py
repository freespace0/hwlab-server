# Generated by Django 2.0 on 2017-12-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0007_state_auto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='auto',
        ),
        migrations.AddField(
            model_name='state',
            name='manual_setting',
            field=models.BooleanField(default=False),
        ),
    ]
