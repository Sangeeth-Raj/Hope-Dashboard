# Generated by Django 5.0.3 on 2024-03-18 06:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0009_alter_problem_options_alter_solution_options'),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.profile'),
        ),
    ]