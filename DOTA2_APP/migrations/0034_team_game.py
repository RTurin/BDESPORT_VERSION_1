# Generated by Django 3.2.7 on 2021-11-03 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0033_tournament_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='game',
            field=models.CharField(blank=True, default='DOTA 2', max_length=100, null=True),
        ),
    ]