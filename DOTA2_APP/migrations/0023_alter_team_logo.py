# Generated by Django 3.2.7 on 2021-10-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0022_auto_20211025_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, default='team/logo/default.png', null=True, upload_to=''),
        ),
    ]
