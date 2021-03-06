# Generated by Django 3.2.7 on 2021-10-05 11:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0004_auto_20211005_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(null=True, verbose_name='date published')),
                ('name', models.CharField(max_length=256)),
                ('rounds', models.IntegerField(default=0)),
                ('start_date', models.DateField(verbose_name='Start date')),
                ('matches_per_day', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('current_round', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Match Date')),
                ('match_number', models.IntegerField(blank=True, null=True)),
                ('match_round', models.IntegerField()),
                ('status', models.CharField(choices=[('BYE', 'BYE'), ('Not Scheduled', 'Not Scheduled'), ('Scheduled', 'Scheduled'), ('Finished', 'Finished')], default='Not Scheduled', max_length=20)),
                ('player_1_score', models.PositiveIntegerField(blank=True, null=True)),
                ('player_2_score', models.PositiveIntegerField(blank=True, null=True)),
                ('fixture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='DOTA2_APP.fixture')),
                ('left_previous', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_next_match', to='DOTA2_APP.match')),
                ('player_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='left_matches', to='DOTA2_APP.tournamentparticipate')),
                ('player_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_matches', to='DOTA2_APP.tournamentparticipate')),
                ('right_previous', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_next_match', to='DOTA2_APP.match')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOTA2_APP.tournament')),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_won', to='DOTA2_APP.tournamentparticipate')),
            ],
            options={
                'verbose_name': 'Matches',
            },
        ),
    ]
