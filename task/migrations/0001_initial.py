# Generated by Django 4.1.5 on 2023-02-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('done', models.CharField(choices=[(1, 'Doing'), (2, 'Done')], max_length=1)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]