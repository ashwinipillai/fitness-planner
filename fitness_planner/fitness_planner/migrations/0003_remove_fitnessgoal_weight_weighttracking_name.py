# Generated by Django 5.0.3 on 2024-03-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_planner', '0002_exercise_execution_steps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitnessgoal',
            name='weight',
        ),
        migrations.AddField(
            model_name='weighttracking',
            name='name',
            field=models.TextField(blank=True, default='Day 1', null=True),
        ),
    ]
