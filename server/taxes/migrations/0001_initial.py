# Generated by Django 5.0.4 on 2024-04-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('income_tax', models.FloatField()),
                ('property_tax', models.FloatField()),
                ('cola_single', models.FloatField()),
                ('cola_four', models.FloatField()),
            ],
        ),
    ]
