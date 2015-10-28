# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import os
import re
import sys

from django.core.files.base import ContentFile
from django.core.management.base import NoArgsCommand, CommandError
from django.db import transaction

from tweet.models import Tweet


def tweet_interpreter(dict_tweet):
    # TODO: verificare se necessario filtrare i twitter con reply !=0 per eliminare i tweet di risposta ad utenti #if not row['reply']
    # TODO: verificare se necessario filtrare i RT
    testo = dict_tweet['testo']    
    #normalizza con valori di default
    dict_tweet.setdefault('tipo',0)    
    dict_tweet.setdefault('stamp',datetime.now().isoformat())    
    ### estrae l'eventuale causa (Es: "(lavori stradali)") e la imposta, se non già presente
    ### se sono presenti più blocchi di testo tra parentesi, non imposta la causa
    cause = re.findall(r'\(([^\)]*)\)',testo)
    causa = cause[0] if len(cause) == 1 else None 
    dict_tweet.setdefault('causa',causa)    
    ### se un tweet inizia con un numero viene escluso perchè contiene info su date future
    if re.match(r'(\d)',testo[0]):
        return [dict_tweet]
    ### se un tweet ha l'hashtag #Milan viene escluso perchè è in inglese (non sempre il filtro sulla lingua funziona)
    if re.search(r'\bMilan\b',testo):
        return [dict_tweet]
    ### se un tweet non contiene almeno un ":", viene escluso
    before,sep,after = testo.partition(':')
    if not sep or not after:
        return [dict_tweet]
    ### prova ad estrarre dal testo prima dei ":" i riferimenti alle Linee
    linee = re.findall (r'(#bus\d+|#tram\d+|#M\d)', before)
    ### se un tweet non ha riferimenti alle Linee, viene escluso
    if not linee:
        return [dict_tweet]
    ### si deve creare un evento per ogni Linea alla quale il Tweet fa riferimento      
    interpreted_tweet=[]
    for linea in linee:
        d = {'stamp': dict_tweet['stamp'],
             'testo': dict_tweet['testo'],
             'causa': causa
             }
        #in codice Linea separa testo e numero e sostituisce con singolo carattere (Es: 'bus58'=>'B58')
        m = re.search(r'\#(\w+)(\d+)',linea)    
        d['linea'] = m.group(1).replace('bus','B').replace('tram','T') + m.group(2)            
        # tipo [0 = non evento, 1 = aperto, 2 = continuazione, 3 = chiuso]
        if re.search(r'riprend|prosegue',after):
            d['tipo'] = 3         #evento di Chiusura
        else:                 ### non è gestito l'evento continuazione: di default sono tutti di apertura = 1            
            d['tipo'] = 1         #evento di Apertura
        interpreted_tweet.append(d)
    return interpreted_tweet

def do_it():
#   for tweet in [Tweet.objects.get(pk=1946)]:
  for tweet in Tweet.objects.filter(causa__isnull=True):
    res = tweet_interpreter({'testo': tweet.testo, 'stamp': tweet.stamp})
    for t in res:
      causa = t.get('causa',None) 
      if causa: 
        print u"{} => {} {}".format(tweet.tipo,causa,t)
        tweet.causa = causa
        tweet.full_clean()
        tweet.save()
  
class Command(NoArgsCommand):
  help = u'Imposta "causa" per Tweet che non l\'hanno già impostata'
  
  def printline(self,msg):
    self.stdout.write(u'{}: {}\n'.format(msg,self.help))
    
  @transaction.atomic
  def handle_noargs(self, **options):
    self.printline('Inizio')
#     transaction.commit_unless_managed()
#     transaction.enter_transaction_management()
#     transaction.managed(True)
    try:
      do_it()
#       transaction.commit()
      self.printline('Fine')
    except Exception, exc:
#       transaction.rollback()
      raise CommandError(self.help + "\n" + str(exc))
#     finally:
#       transaction.leave_transaction_management()
