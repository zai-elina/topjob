# Generated by Django 4.1.5 on 2023-04-16 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_rename_task_interview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interview',
            options={'ordering': ['task_date'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
