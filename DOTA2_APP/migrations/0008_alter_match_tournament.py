# Generated by Django 3.2.7 on 2021-10-05 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0007_tournamentparticipate_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOTA2_APP.tournament'),
        ),
    ]