from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index



class Equipo(Page):

    # Database fields

    body = RichTextField()
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    # Search index configuration

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]


    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('feed_image'),
    ]


    # Parent page / subpage type rules

    parent_page_types = ['formula1.Listado']
    subpage_types = []


class Listado(Page):

    body = RichTextField()


    # Search index configuration

    search_fields = Page.search_fields + [
        index.SearchField('body'),

    ]


    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
