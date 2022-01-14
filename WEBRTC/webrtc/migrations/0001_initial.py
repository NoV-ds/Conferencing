# Generated by Django 3.2 on 2022-01-05 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomProperties',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('enable_new_call_ui', models.BooleanField(default='True')),
                ('enable_prejoin_ui', models.BooleanField(null=True)),
                ('enable_knocking', models.BooleanField(default='False')),
                ('enable_screenshare', models.BooleanField(default='True')),
                ('enable_video_processing_ui', models.BooleanField(default='True')),
                ('enable_chat', models.BooleanField(default='False')),
                ('start_video_off', models.BooleanField(default='False')),
                ('start_audio_off', models.BooleanField(default='False')),
                ('owner_only_broadcast', models.BooleanField(default='False')),
                ('is_owner', models.BooleanField(default='False')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(default='INDIA', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('api_created', models.BooleanField(default=True)),
                ('privacy', models.CharField(default='public', max_length=50)),
                ('token', models.CharField(blank=True, max_length=200)),
                ('url', models.URLField()),
                ('created_at', models.CharField(max_length=100)),
                ('Participants', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participants_users', to=settings.AUTH_USER_MODEL)),
                ('properties', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webrtc.roomproperties')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]