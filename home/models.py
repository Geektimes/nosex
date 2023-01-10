from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import StreamField
from wagtail import blocks

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("time", blocks.CharBlock(required=True, max_length=40)),
                ("title", blocks.CharBlock(required=True, max_length=200)),
                ("image", ImageChooserBlock(required=True)),
                ("leader", blocks.TextBlock(required=True, max_length=100)),
            ]
        )
    )

    class Meta:
        template = "card_block.html"
        icon = "placeholder"
        label = "Staff Cards"

class GuestBlock(blocks.StructBlock):
    """Guest with image and text."""
    guests = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("name", blocks.TextBlock(required=True, max_length=100)),
                ("prof", blocks.TextBlock(required=True, max_length=100)),
            ]
        )
    )

    class Meta:
        template = "guest_block.html"
        icon = "placeholder"
        label = "Guests Cards"

class HomePage(Page):
    # поля в БД
    date_event = models.CharField(
        null=True,
        blank=True,
        max_length=50,
        verbose_name='Дата события (в шапке)'
    )

    telegram = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )

    email = models.CharField(
        null=True,
        blank=True,
        max_length=50,
    )

    head_location = models.CharField(
        null=True,
        blank=True,
        max_length=200,
        verbose_name = 'Название локации (в шапке)'
    )

    adress = models.CharField(
        null=True,
        blank=True,
        max_length=200
    )

    about_body = models.TextField(
        null=True,
        blank=True,
        verbose_name='Заметка "О нас"'
    )

    about_img = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name='Изображение в блоке "О нас"'
    )

    book_title = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name='Второй заголовок в блоке "О нас"'
    )

    book_body = models.TextField(
        null=True,
        blank=True,
        verbose_name='Вторая заметка в блоке "О нас"'
    )

    guests = StreamField([
        ("guests", GuestBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
        verbose_name='Карточки гостей (в блоке "Гости")'
    )

    schedule = StreamField([
        ("cards", CardBlock()),
        ],
        null=True,
        blank=True,
        use_json_field=True,
        verbose_name='Карточки-Пункты "Расписания"'
    )

    # поля в интерфейсе админа для ввода данных
    content_panels = Page.content_panels + [
        FieldPanel('date_event'),
        FieldPanel('head_location'),
        FieldPanel('about_body'),
        FieldPanel('about_img'),
        FieldPanel('book_title'),
        FieldPanel('book_body'),
        FieldPanel('adress'),
        FieldPanel('telegram'),
        FieldPanel('email'),
        FieldPanel('schedule'),
        FieldPanel('guests'),
    ]