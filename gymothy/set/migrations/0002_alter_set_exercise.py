# Generated by Django 4.2.5 on 2023-11-28 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_remove_exercise_rep_num_remove_exercise_set_num_and_more'),
        ('set', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='set',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='exercise.exercise'),
        ),
    ]
