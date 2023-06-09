# Generated by Django 4.1.7 on 2023-06-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0017_visitorlog1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organisationcheckin',
            name='meeting_duration_time',
        ),
        migrations.AddField(
            model_name='organisationcheckin',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='organisationcheckin',
            name='visitor_item_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='visitorlog',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
