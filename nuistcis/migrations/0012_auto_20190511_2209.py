# Generated by Django 2.2.1 on 2019-05-11 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuistcis', '0011_auto_20190511_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='new_author',
            field=models.CharField(default='Raeed', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='news_content',
            field=models.TextField(max_length=5000),
        ),
    ]
