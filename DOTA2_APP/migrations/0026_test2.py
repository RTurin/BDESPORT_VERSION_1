# Generated by Django 3.2.7 on 2021-10-26 13:28

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('DOTA2_APP', '0025_alter_team_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='test2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_title', models.CharField(blank=True, max_length=100, null=True)),
                ('image_upload_ResizedImageField', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[1920, 1080], upload_to='')),
                ('image_upload_default', models.ImageField(upload_to='')),
            ],
        ),
    ]
