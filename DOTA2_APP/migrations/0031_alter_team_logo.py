# Generated by Django 3.2.7 on 2021-10-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0030_alter_team_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
