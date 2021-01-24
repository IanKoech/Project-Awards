# Generated by Django 3.1.5 on 2021-01-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profilepic', models.ImageField(upload_to='profiles/')),
                ('bio', models.TextField()),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
    ]