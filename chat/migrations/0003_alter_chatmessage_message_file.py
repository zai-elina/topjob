# Generated by Django 4.1.5 on 2023-06-01 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_chatmessage_message_chatmessage_message_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='message_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]