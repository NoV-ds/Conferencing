from django.urls import path
from .views import *

urlpatterns = [
    # path('', rooms, name='rooms'),
    path('<uuid:metting_id>/', index, name='index'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('signup/', Signup, name='signup'),
    path('profile/', Profile_Details, name='profile'),
    path('create-room/', create_rooms, name='create-room'),
    path('room/<str:name>', roomDetails, name='room'),
    path('update-room/', updateRoom, name='update-room'),
    path('rooms/', roomss, name='roomss')
]