# Generated by Django 5.0.3 on 2024-03-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0004_therapist_contact_number_therapist_joined_from_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='therapist',
            old_name='locatoin',
            new_name='location',
        ),
        migrations.AlterField(
            model_name='therapist',
            name='total_solutions_posted',
            field=models.IntegerField(null=True),
        ),
    ]
