# Generated by Django 2.2.5 on 2019-09-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='code',
            field=models.TextField(default='okiplus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='title',
            field=models.CharField(default='OkiPlus', max_length=20),
            preserve_default=False,
        ),
    ]
