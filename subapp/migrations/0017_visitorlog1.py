# Generated by Django 4.1.7 on 2023-06-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0016_visitorlog_visitor_item_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitorLog1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(blank=True, max_length=100, null=True)),
                ('vehicle_number', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
