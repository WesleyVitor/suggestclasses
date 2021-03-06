# Generated by Django 3.0.4 on 2020-04-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_funcaogratificada_turmaestendida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.IntegerField()),
                ('nome_discente', models.CharField(max_length=200)),
                ('sexo', models.CharField(max_length=1)),
                ('ano_ingresso', models.IntegerField()),
                ('periodo_ingresso', models.IntegerField()),
                ('forma_ingresso', models.CharField(max_length=100)),
                ('tipo_discente', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('sigla_nivel_ensino', models.CharField(max_length=5)),
                ('nivel_ensino', models.CharField(max_length=50)),
                ('id_curso', models.CharField(max_length=100)),
                ('nome_curso', models.CharField(max_length=200)),
                ('modalidade_educacao', models.CharField(max_length=50)),
                ('id_unidade', models.IntegerField()),
                ('nome_unidade', models.CharField(max_length=200)),
                ('id_unidade_gestora', models.IntegerField()),
                ('nome_unidade_gestora', models.CharField(max_length=200)),
            ],
        ),
    ]
