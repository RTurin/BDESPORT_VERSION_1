# Generated by Django 3.2.7 on 2021-10-31 15:15

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0032_alter_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='remark',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
