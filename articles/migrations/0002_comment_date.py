# Generated by Django 3.0.5 on 2020-04-24 14:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 4, 24, 14, 42, 8, 56558, tzinfo=utc)),
            preserve_default=False,
        ),
    ]