# Generated by Django 4.2.1 on 2023-06-17 12:09

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formula1', '0007_equipo_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='formula1.champcategory'),
        ),
    ]
