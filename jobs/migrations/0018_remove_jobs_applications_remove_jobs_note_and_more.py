# Generated by Django 4.1.5 on 2023-05-02 20:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0017_alter_company_companylogo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='applications',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='note',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='salary',
        ),
        migrations.AddField(
            model_name='company',
            name='addressLine',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='inn',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Это поле должно содержать только цифры.'), django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AddField(
            model_name='company',
            name='ogrn',
            field=models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Это поле должно содержать только цифры.'), django.core.validators.MinLengthValidator(13)]),
        ),
        migrations.AddField(
            model_name='company',
            name='ogrnip',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Это поле должно содержать только цифры.'), django.core.validators.MinLengthValidator(15)]),
        ),
        migrations.AddField(
            model_name='company',
            name='url',
            field=models.URLField(blank=True, max_length=128, null=True, verbose_name='Ссылка на сайт'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='max_salary',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='min_salary',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='experience',
            field=models.CharField(choices=[('Нет опыта', 'Нет опыта'), ('Меньше 2 лет', 'Меньше 2 лет'), ('2-5 лет', 'от 2 до 5 лет'), ('5-10 лет', 'от 5 до 10 лет'), ('10-15 лет', 'от 10 до 15 лет'), ('>15 лет', 'Больше 15 лет')], default='Меньше 2 лет', max_length=100),
        ),
    ]
