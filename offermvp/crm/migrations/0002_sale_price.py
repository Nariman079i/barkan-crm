# Generated by Django 4.1.6 on 2023-03-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
