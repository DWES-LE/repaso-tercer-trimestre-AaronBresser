# Generated by Django 4.2.1 on 2023-06-14 09:46

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0004_remove_equipo_date_equipo_campeonatos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listado',
            name='body',
        ),
        migrations.AddField(
            model_name='listado',
            name='jefe_equipo',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
