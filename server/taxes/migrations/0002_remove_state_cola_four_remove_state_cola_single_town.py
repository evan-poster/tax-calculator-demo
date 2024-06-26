# Generated by Django 5.0.4 on 2024-04-09 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='cola_four',
        ),
        migrations.RemoveField(
            model_name='state',
            name='cola_single',
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cola_single', models.FloatField()),
                ('cola_four', models.FloatField()),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taxes.state')),
            ],
        ),
    ]
