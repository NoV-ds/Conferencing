# Generated by Django 3.2 on 2022-01-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webrtc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]