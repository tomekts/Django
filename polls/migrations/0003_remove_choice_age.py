# Generated by Django 3.1.5 on 2021-01-14 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='age',
        ),
    ]
