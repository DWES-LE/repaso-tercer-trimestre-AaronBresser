from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index



class Equipo(Page):

    # Database fields

    body = RichTextField()
    fundacion = models.DateField("Fecha fundación", blank=True, null=True)
    pais = models.CharField(max_length=255, blank=True, null=True)
    jefe_equipo = models.CharField(max_length=255, blank=True, null=True)
    motor = models.CharField(max_length=255, blank=True, null=True)
    pilotos = models.CharField(max_length=255, blank=True, null=True)
    campeonatos = models.IntegerField(blank=True, null=True)
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
        index.FilterField('fundacion'),
        index.FilterField('pais'),
        index.FilterField('jefe_equipo'),
        index.FilterField('motor'),
        index.FilterField('pilotos'),
        index.FilterField('campeonatos'),
    ]


    # Editor panels configuration

    content_panels = Page.content_panels + [
        FieldPanel('fundacion'),
        FieldPanel('body'),
        FieldPanel('feed_image'),
        FieldPanel('pais'),
        FieldPanel('jefe_equipo'),
        FieldPanel('motor'),
        FieldPanel('pilotos'),
        FieldPanel('campeonatos'),
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
