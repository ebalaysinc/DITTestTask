# Generated by Django 5.1.1 on 2024-09-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_chapter_original'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='link',
            field=models.TextField(default='https://test.link/'),
            preserve_default=False,
        ),
    ]
