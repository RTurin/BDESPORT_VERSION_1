# Generated by Django 3.2.7 on 2021-10-25 14:27

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0024_alter_team_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='team/logo/default.png', force_format='PNG', keep_meta=True, quality=75, size=[500, 300], upload_to='team/logo/'),
        ),
    ]
