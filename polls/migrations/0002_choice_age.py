# Generated by Django 3.1.5 on 2021-01-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
