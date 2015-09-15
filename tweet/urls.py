# coding: utf-8

from django.conf.urls import patterns, include, url
from rest_framework.routers import SimpleRouter

from .views import TweetViewSet


router = SimpleRouter()

##### Elenco endpoints ################################
router.register(r'tweet', TweetViewSet)


##### Aggiunta degli url ####################################
urlpatterns =  patterns('',
    url(r'^', include(router.urls)),
)

