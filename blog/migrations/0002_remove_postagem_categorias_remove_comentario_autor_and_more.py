# Generated by Django 5.1.6 on 2025-02-27 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postagem',
            name='Categorias',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postagem',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='postagem',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.DeleteModel(
            name='Postagem',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
