# Generated by Django 5.0.3 on 2024-03-11 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_planner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='execution_steps',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
