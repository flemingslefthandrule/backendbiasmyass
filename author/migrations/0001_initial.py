# Generated by Django 5.0.3 on 2024-03-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=500)),
                ('photo', models.CharField(max_length=100)),
                ('url', models.SlugField(max_length=100, unique=True)),
            ],
        ),
    ]
