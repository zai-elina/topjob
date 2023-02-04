# Generated by Django 4.1.5 on 2023-02-04 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_jobs_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='experience',
            field=models.CharField(choices=[('Меньше 2 лет', 'Меньше 2 лет'), ('2-5 лет', 'от 2 до 5 лет'), ('5-10 лет', 'от 5 до 10 лет'), ('10-15 лет', 'от 10 до 15 лет'), ('>15 лет', 'Больше 15 лет')], default='Меньше 2 лет', max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='type',
            field=models.CharField(choices=[('Полный', 'Полная'), ('Неполный', 'Неполная'), ('Удаленно', 'Удаленно')], default='Полный', max_length=50),
        ),
    ]
