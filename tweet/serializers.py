from .models import Tweet
from rest_framework import serializers


class TweetSerializer(serializers.ModelSerializer):
  tipo_evento = serializers.SerializerMethodField('get_evento') 


  def get_evento(self,obj):
    print(obj.get_tipo_display())
    return obj.get_tipo_display()

  class Meta:
    model = Tweet
    fields = '__all__'
