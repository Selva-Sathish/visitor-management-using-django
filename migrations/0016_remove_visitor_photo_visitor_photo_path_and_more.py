# Generated by Django 5.0.2 on 2024-02-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0015_alter_visitor_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitor',
            name='photo',
        ),
        migrations.AddField(
            model_name='visitor',
            name='photo_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='person_to_meet',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='purpose',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='visitor_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]