# Generated by Django 4.1.7 on 2023-03-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('engine', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
