# Generated by Django 5.0.3 on 2024-03-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chief', '0024_therapist_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True),
        ),
    ]
