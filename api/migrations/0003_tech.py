# Generated by Django 3.0.5 on 2020-04-21 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200421_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=100)),
                ('tech_lvl', models.CharField(max_length=100)),
                ('offert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technology', to='api.Offert')),
            ],
        ),
    ]
