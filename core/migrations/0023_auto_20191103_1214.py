# Generated by Django 2.1.7 on 2019-11-03 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20191024_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacaocurricular',
            name='id_curriculo_componente',
            field=models.IntegerField(unique=True),
        ),
    ]
