# Generated by Django 4.1.5 on 2023-04-14 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_alter_category_categoryimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='summary',
        ),
    ]