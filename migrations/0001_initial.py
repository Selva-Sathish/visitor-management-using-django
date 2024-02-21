# Generated by Django 5.0.2 on 2024-02-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vistior_Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Visitor_name', models.CharField(blank=True, max_length=30, null=True)),
                ('Mobile_no', models.IntegerField()),
                ('Place', models.CharField(blank=True, max_length=50, null=True)),
                ('Company_name', models.CharField(blank=True, max_length=30, null=True)),
                ('Designation', models.CharField(blank=True, max_length=30, null=True)),
                ('To_meet', models.CharField(choices=[(1, 'MD'), (2, 'Manager')], default=1, max_length=15)),
                ('Purpose_to_meet', models.TextField(blank=True, null=True)),
            ],
        ),
    ]