# Generated by Django 4.2.6 on 2023-11-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-02-25'),
            preserve_default=False,
        ),
    ]
