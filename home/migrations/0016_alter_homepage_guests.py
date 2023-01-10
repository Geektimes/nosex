# Generated by Django 4.1.5 on 2023-01-06 19:23

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_homepage_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='guests',
            field=wagtail.fields.StreamField([('guests', wagtail.blocks.StructBlock([('guests', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('name', wagtail.blocks.TextBlock(max_length=100, required=True)), ('prof', wagtail.blocks.TextBlock(max_length=100, required=True))])))]))], blank=True, null=True, use_json_field=True),
        ),
    ]
