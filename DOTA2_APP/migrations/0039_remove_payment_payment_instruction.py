# Generated by Django 3.2.7 on 2021-11-05 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0038_payment_sumbitted_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='payment_Instruction',
        ),
    ]
