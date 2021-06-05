# Generated by Django 3.1.7 on 2021-06-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210604_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_subtitle',
            field=models.CharField(default='文章简介', max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='picurl',
            field=models.CharField(default='url', max_length=300),
        ),
    ]