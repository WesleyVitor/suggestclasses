# Generated by Django 2.2.7 on 2019-11-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20191125_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='data_consolidacao',
            field=models.DateField(null=True),
        ),
    ]
