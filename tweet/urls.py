# coding: utf-8

from django.urls import re_path as url, include
from rest_framework.routers import SimpleRouter

from .views import TweetViewSet


router = SimpleRouter()

##### Elenco endpoints ################################
router.register(r'tweet', TweetViewSet)


##### Aggiunta degli url ####################################
app_name = 'tweet'
urlpatterns =  [
    url(r'^', include(router.urls)),
]

