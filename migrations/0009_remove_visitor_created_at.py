# Generated by Django 5.0.2 on 2024-02-13 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0008_visitor_delete_capturedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='created_at',
        ),
    ]
