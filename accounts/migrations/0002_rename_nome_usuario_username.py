# Generated by Django 5.1.6 on 2025-02-27 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='nome',
            new_name='username',
        ),
    ]
