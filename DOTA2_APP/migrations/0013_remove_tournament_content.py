# Generated by Django 3.2.7 on 2021-10-23 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0012_tournament_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='content',
        ),
    ]
