# Generated by Django 5.0.3 on 2024-03-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_rename_url_author_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
