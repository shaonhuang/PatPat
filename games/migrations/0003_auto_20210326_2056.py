# Generated by Django 3.1.7 on 2021-03-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_auto_20210326_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameinfo',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
