# Generated by Django 5.0.2 on 2024-02-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0009_remove_visitor_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='purpose',
            field=models.CharField(max_length=100),
        ),
    ]
