# Generated by Django 2.2.4 on 2019-08-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('genero', models.CharField(choices=[('M', 'Macho'), ('F', 'Femia')], max_length=255, verbose_name='Gênero')),
                ('especie', models.CharField(choices=[('G', 'Gato'), ('C', 'Cachorro'), ('A', 'Ave')], max_length=255, verbose_name='Especie')),
                ('ativo', models.BooleanField(default=True)),
                ('data_de_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
