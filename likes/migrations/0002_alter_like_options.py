# Generated by Django 3.2.16 on 2023-01-17 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'ordering': ['-created_at']},
        ),
    ]
