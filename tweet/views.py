from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response

from .models import Tweet
from .serializers import TweetSerializer


# Decoratore #####################################
#################################################
def build_message_response(message,status=HttpResponse.status_code):
  return Response({'message': message},status=status)

#################################################
class RESPERR(object):
  GENERIC_ERROR = 'GENERIC_ERROR'

def build_error_response(error,status=HttpResponseBadRequest.status_code,message=None):
  return Response({'error': error, 'message': message},status=status)

#################################################
def build_exception_response(error=RESPERR.GENERIC_ERROR,status=HttpResponseBadRequest.status_code):
    import traceback
    return build_error_response(error,status,message=traceback.format_exc())


class TweetViewSet(viewsets.ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all().order_by('-stamp',)

    @list_route(methods=['PUT'])
    def upload(self, request):
      try:          
          serializer_class = self.get_serializer_class()  
          serializer = serializer_class(data=request.DATA, many=True, partial=True,
                                        allow_add_remove=False)
          if serializer.is_valid():
              serializer.save()                                                
              return build_message_response('OK')
          else:
              return build_error_response(serializer.errors)
      except Exception, exc:
          return build_exception_response()
        