# Generated by Django 4.2.5 on 2023-11-01 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0002_tag_exercise_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='rep_num',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='set_num',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='weight_num',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='weight_type',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
