# Generated by Django 4.1.5 on 2023-04-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_remove_jobs_owner_company_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='applications',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='summary',
            field=models.TextField(null=True),
        ),
    ]
