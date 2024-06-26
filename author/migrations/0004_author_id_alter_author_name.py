# Generated by Django 5.0.3 on 2024-03-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_remove_author_id_alter_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
