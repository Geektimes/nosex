# Generated by Django 4.1.5 on 2023-01-06 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_remove_homepage_rtf_body_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='content',
            new_name='schedule',
        ),
    ]
