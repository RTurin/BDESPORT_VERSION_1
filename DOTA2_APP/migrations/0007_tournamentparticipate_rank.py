# Generated by Django 3.2.7 on 2021-10-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0006_tournamentparticipate_fixture'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentparticipate',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
