# Generated by Django 2.2.5 on 2019-10-22 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('cod_artigo', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('resumo', models.CharField(max_length=3000)),
                ('palavras_cha', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=100)),
                ('situacao', models.CharField(max_length=30)),
                ('pdf', models.FileField(upload_to='artigos/pdfs')),
            ],
        ),
    ]
