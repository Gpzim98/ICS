# Generated by Django 5.1 on 2024-09-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=50)),
                ('sobrenome', models.TextField(max_length=80)),
                ('endereco', models.TextField(max_length=150)),
                ('data_nascimento', models.TextField(max_length=10)),
            ],
        ),
    ]