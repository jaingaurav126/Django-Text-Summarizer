# Generated by Django 2.0.5 on 2018-07-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summarizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summary',
            name='original_link',
            field=models.TextField(),
        ),
    ]