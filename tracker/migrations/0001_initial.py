# Generated by Django 4.1.4 on 2022-12-22 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now=True)),
                ('Description', models.CharField(max_length=60)),
                ('Amount', models.IntegerField()),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]