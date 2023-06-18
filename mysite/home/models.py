from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class ContactPage(Page):
    intro = RichTextField(blank=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('email'),
        FieldPanel('telefono'),
        FieldPanel('direccion'),
    ]

class AcercaDe(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

