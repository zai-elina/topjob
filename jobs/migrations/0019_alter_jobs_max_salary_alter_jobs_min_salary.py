# Generated by Django 4.1.5 on 2023-05-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_remove_jobs_applications_remove_jobs_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='max_salary',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='min_salary',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=12, null=True),
        ),
    ]