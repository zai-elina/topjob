# Generated by Django 4.1.5 on 2023-02-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='summary',
            field=models.TextField(),
        ),
    ]
