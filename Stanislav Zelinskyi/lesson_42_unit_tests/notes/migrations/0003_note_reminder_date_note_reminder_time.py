# Generated by Django 4.2.2 on 2023-06-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_category_note_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='reminder_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='reminder_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]