# Generated by Django 2.1.2 on 2018-10-15 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20181015_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='affected_system',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='assigned_technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_technician', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='attached_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='date',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='module',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='priority',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='subject',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='type',
            field=models.TextField(blank=True, null=True),
        ),
    ]