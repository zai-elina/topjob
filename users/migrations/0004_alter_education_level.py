# Generated by Django 4.1.5 on 2023-02-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_resume_addressline1_alter_resume_addressline2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='level',
            field=models.CharField(choices=[('Среднее образование', 'Среднее образование'), ('Среднее профессиональное образование', 'Среднее профессиональное образование'), ('Бакалавриат высшего образования', 'Бакалавриат высшего образования'), ('Специалитет высшего образования', 'Специалитет высшего образования'), ('Магистратура высшего образования', 'Магистратура высшего образования'), ('Аспирантура', 'Аспирантура'), ('Докторская степень', 'Докторская степень'), ('Сертификат', 'Сертификат')], default='Среднее образование', max_length=200),
        ),
    ]
