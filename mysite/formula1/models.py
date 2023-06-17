from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django import forms

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index



class Listado(Page):
    jefe_equipo = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        listadopages = self.get_children().live().order_by('-first_published_at')
        context['listadopages'] = listadopages
        return context

class Equipo(Page):

    # Database fields

    body = RichTextField()
    fundacion = models.DateField("Fecha fundación", blank=True, null=True)
    pais = models.CharField(max_length=255, blank=True, null=True)
    jefe_equipo = models.CharField(max_length=255, blank=True, null=True)
    motor = models.CharField(max_length=255, blank=True, null=True)
    pilotos = models.CharField(max_length=255, blank=True, null=True)
    campeonatos = models.IntegerField(blank=True, null=True)
    categories = ParentalManyToManyField('formula1.ChampCategory', blank=True)
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
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]

@register_snippet
class ChampCategory(models.Model):
    nombre = models.CharField(max_length=255)
    icono = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('nombre'),
        FieldPanel('icono'),
    ]

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'champ categories'

