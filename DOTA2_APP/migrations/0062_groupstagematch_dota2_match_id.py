# Generated by Django 3.2.7 on 2021-11-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0061_alter_groupstagematch_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupstagematch',
            name='dota2_match_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
