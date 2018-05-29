# -*- coding: utf-8 -*-


from django.contrib.gis.db import models


#from django.db import models
#from django.contrib.auth.models import User
class Tweet (models.Model):
	TIPO = (
        (0, 'Non evento'),
        (1, 'Apertura'),
        (2, 'Continuazione'),
        (3, 'Chiusura'),
	)
	tipo = models.IntegerField(choices=TIPO, null=False,blank=False)
	stamp = models.DateTimeField(auto_now=False, null=False,blank=False)
	stamp_evento = models.DateTimeField(auto_now=False, null=True,blank=True)
	root_tweet = models.ForeignKey('self', null=True,blank=True, on_delete=models.CASCADE)
	linea = models.CharField(max_length=50, null=True,blank=True)
	causa = models.CharField(max_length=100, null=True,blank=True)
	testo = models.CharField(max_length=250, null=False,blank=False)

	class Meta: # creare la classe meta per sistemare il plurale dell admin
		verbose_name_plural = "Tweet rilevati dallo stream di ATM"
		
	def __unicode__(self):
		return u'%s_%s_%s' %(self.stamp, self.tipo, self.linea)
