# Generated by Django 3.2.7 on 2021-11-05 15:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0036_tournament_payment_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='remark',
            field=ckeditor.fields.RichTextField(blank=True, default='', null=True),
        ),
    ]
