# Generated by Django 3.2 on 2023-05-03 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20230205_0719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('year',), 'verbose_name': 'Title', 'verbose_name_plural': 'Titles'},
        ),
        migrations.AlterField(
            model_name='title',
            name='name',
            field=models.CharField(db_index=True, max_length=90, verbose_name='title name'),
        ),
    ]
