# Generated by Django 3.1.7 on 2021-03-10 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentario', '0001_initial'),
        ('avaliacao', '0001_initial'),
        ('pontosturisticos', '0003_pontoturistico_atracoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacao.Avaliacao'),
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='comentarios',
            field=models.ManyToManyField(to='comentario.Comentario'),
        ),
    ]
