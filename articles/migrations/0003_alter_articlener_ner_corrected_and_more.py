# Generated by Django 4.1.2 on 2022-10-08 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articlener'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlener',
            name='ner_corrected',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articlener',
            name='ner_raw',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
