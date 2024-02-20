# Generated by Django 2.2.1 on 2019-06-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuistcis', '0029_excellentscholar'),
    ]

    operations = [
        migrations.AddField(
            model_name='excellentscholar',
            name='scholar_description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='excellentscholar',
            name='scholar_facebook',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='excellentscholar',
            name='scholar_job',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='excellentscholar',
            name='scholar_linkedin',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='excellentscholar',
            name='scholar_wechat',
            field=models.CharField(max_length=500),
        ),
    ]
