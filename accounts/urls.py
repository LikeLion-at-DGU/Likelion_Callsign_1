from urllib.parse import urlparse
from django.urls import path, include
from .views import *

app_name = "accounts"
urlpatterns = [
    path('logout/', logout, name="logout"),
        
    path('mypost_list/', mypostlist, name="mypost_list"),
    path('mylikepost_list/', mylikelist, name="mylikepost_list"),
    
    path('newinfo/', newinfo, name= 'newinfo'),
    path('information/', information, name="information"),
]