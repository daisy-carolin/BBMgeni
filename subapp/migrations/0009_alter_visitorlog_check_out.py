# Generated by Django 4.1.7 on 2023-05-12 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0008_remove_organisationaladmin_fields_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitorlog',
            name='check_out',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
