# Generated by Django 2.2.1 on 2019-05-24 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nuistcis', '0022_auto_20190525_0233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programs',
            old_name='Programs_type',
            new_name='programs_type',
        ),
    ]