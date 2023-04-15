# Generated by Django 4.1.5 on 2023-04-15 13:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_favorite_options_alter_favorite_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='soft_skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='profession',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resume',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='uniqueId',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
