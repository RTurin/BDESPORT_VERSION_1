# Generated by Django 3.2.7 on 2021-10-25 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0015_player_estimated_mmr'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentparticipate',
            name='text_teamName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
