# Generated by Django 5.0.3 on 2024-03-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0004_author_id_alter_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='summary',
            field=models.CharField(default='whatasuddensuppaise', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='url',
            field=models.CharField(default='https://www.google.com', max_length=500),
            preserve_default=False,
        ),
    ]
