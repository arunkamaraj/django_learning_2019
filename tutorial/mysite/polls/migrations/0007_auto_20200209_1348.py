# Generated by Django 2.2 on 2020-02-09 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['age']},
        ),
    ]
