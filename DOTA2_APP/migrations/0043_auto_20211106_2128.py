# Generated by Django 3.2.7 on 2021-11-06 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0042_payment_tranx_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='stage',
            field=models.CharField(blank=True, choices=[('Group Stage', 'Group Stage'), ('PlayOffs', 'PlayOffs')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('BYE', 'BYE'), ('Not Scheduled', 'Not Scheduled'), ('Scheduled', 'Scheduled'), ('Finished', 'Finished')], default='Not Scheduled', max_length=30),
        ),
        migrations.CreateModel(
            name='GroupStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchdate', models.DateField()),
                ('group', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B')], max_length=5, null=True)),
                ('series_Type', models.CharField(blank=True, choices=[('BO1', 'BO1'), ('BO2', 'BO2'), ('BO3', 'BO3')], max_length=5, null=True)),
                ('match', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='DOTA2_APP.match')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOTA2_APP.tournament')),
            ],
        ),
    ]