# Generated by Django 2.1.2 on 2018-10-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20181018_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='isTechnician',
            field=models.BooleanField(default=False),
        ),
    ]
