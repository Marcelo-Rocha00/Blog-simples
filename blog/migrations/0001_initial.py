# Generated by Django 5.1.6 on 2025-02-24 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('conteudo', models.TextField()),
                ('imagens', models.ImageField(blank=True, upload_to='')),
                ('status_postagem', models.CharField(choices=[('R', ' Rascunho'), ('P', ' Postado ')], max_length=1)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_publicação', models.DateTimeField(auto_now=True)),
                ('Categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.usuario')),
                ('tags', models.ManyToManyField(blank=True, to='blog.tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('status', models.CharField(choices=[('PE', 'Pendente'), ('AP', 'Aprovado'), ('RE', 'Rejeitado')], max_length=2)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.usuario')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.postagem')),
            ],
        ),
    ]
