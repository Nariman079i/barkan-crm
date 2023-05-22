# Generated by Django 4.1.6 on 2023-05-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barkan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='service',
        ),
        migrations.AddField(
            model_name='guide',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='history',
            name='feedback',
            field=models.CharField(max_length=255, null=True),
        ),
    ]