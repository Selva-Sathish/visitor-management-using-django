# Generated by Django 5.0.2 on 2024-02-12 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vistior_management',
            name='Mobile_no',
        ),
        migrations.AddField(
            model_name='vistior_management',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
