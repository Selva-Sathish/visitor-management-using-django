# Generated by Django 5.0.2 on 2024-02-15 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0011_alter_visitor_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='photo',
        ),
    ]