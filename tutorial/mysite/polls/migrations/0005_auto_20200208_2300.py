# Generated by Django 2.2 on 2020-02-08 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200208_2257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publications',
            new_name='Publication',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='publication',
            new_name='publications',
        ),
    ]
