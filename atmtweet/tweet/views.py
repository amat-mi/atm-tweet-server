from django.shortcuts import render
from .serializers import TweetSerializer
from .models import Tweet
from rest_framework import viewsets
import django_filters

# Decoratore #####################################
from rest_framework.decorators import list_route





class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()

    @list_route(methods=['PUT'])
    def upload(self, request):
      try:          
          serializer_class = self.get_serializer_class()  
          serializer = serializer_class(self.get_queryset(),
                                        data=request.DATA, many=True, partial=False,
                                        allow_add_remove=False)
          if serializer.is_valid():
              serializer.save()                                                
              return build_message_response('OK')
          else:
              return build_error_response(serializer.errors)
      except Exception, exc:
          return build_exception_response()
        

