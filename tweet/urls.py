from django.conf.urls import patterns, include, url
from .views import TweetViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

##### Elenco endpoints ################################
router.register(r'tweet', TweetViewSet)


##### Aggiunta degli url ####################################
urlpatterns =  patterns('',
    url(r'^', include(router.urls)),
    
)

