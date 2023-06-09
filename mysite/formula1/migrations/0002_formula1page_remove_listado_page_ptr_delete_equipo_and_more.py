# Generated by Django 4.2.1 on 2023-06-11 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('formula1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formula1Page',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'Formula1 Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='listado',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='Equipo',
        ),
        migrations.DeleteModel(
            name='Listado',
        ),
    ]
