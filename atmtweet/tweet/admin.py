from django.contrib import admin

from .models import Tweet

# Register your models here.



class TweetAdmin(admin.ModelAdmin):
    list_display = ('tipo','stamp', 'stamp_evento', 'root_tweet', 'linea','testo',)
    #list_filter = ['categoria', 'collezione', 'price', ]
    fieldsets = [
        (None, {
            'fields': ('tipo','stamp', 'stamp_evento', 'root_tweet', 'linea','testo',),
            
            }),
    ]

admin.site.register(Tweet, TweetAdmin)

