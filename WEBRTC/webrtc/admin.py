from django.contrib import admin
from .models import UserProfile, Room, RoomProperties

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Room)
admin.site.register(RoomProperties)