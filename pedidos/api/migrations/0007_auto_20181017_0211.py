# Generated by Django 2.1.2 on 2018-10-17 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20181015_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='es_tecnico',
            field=models.BooleanField(default=True),
        ),
    ]
