# Generated by Django 2.2.1 on 2019-05-23 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nuistcis', '0017_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='new_author',
            new_name='note_author',
        ),
    ]
