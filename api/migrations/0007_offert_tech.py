# Generated by Django 3.0.5 on 2020-04-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_offert_tech'),
    ]

    operations = [
        migrations.AddField(
            model_name='offert',
            name='tech',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]