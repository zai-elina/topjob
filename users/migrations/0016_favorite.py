# Generated by Django 4.1.5 on 2023-04-13 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_alter_applicant_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0015_remove_resume_cover_letter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobs')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
