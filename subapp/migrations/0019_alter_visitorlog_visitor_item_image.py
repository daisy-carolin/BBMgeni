# Generated by Django 4.1.7 on 2023-06-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0018_remove_organisationcheckin_meeting_duration_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorlog',
            name='visitor_item_image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
