# Generated by Django 3.1.5 on 2021-01-27 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awardsapp', '0003_auto_20210127_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='Landing',
            field=models.ImageField(upload_to='landings/'),
        ),
    ]
