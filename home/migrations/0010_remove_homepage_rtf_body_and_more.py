# Generated by Django 4.1.5 on 2023-01-06 15:14

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_homepage_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='rtf_body',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='schedule_block',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='str_body',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='subtitle',
        ),
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.fields.StreamField([('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(max_length=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
