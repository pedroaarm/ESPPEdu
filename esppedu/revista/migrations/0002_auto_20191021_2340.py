# Generated by Django 2.2.5 on 2019-10-22 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artigo',
            old_name='palavras_cha',
            new_name='palavras_chaves',
        ),
    ]