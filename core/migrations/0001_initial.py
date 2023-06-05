# Generated by Django 4.2.1 on 2023-06-05 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('dataCriacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sexo', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=255)),
                ('logradouro', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Groups', to='core.grupo')),
            ],
        ),
    ]
