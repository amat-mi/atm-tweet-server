# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.IntegerField(max_length=1, choices=[(0, b'Non evento'), (1, b'Apertura'), (2, b'Continuazione'), (3, b'Chiusura')])),
                ('stamp', models.DateTimeField()),
                ('stamp_evento', models.DateTimeField(null=True, blank=True)),
                ('linea', models.CharField(max_length=b'50', null=True, blank=True)),
                ('testo', models.CharField(max_length=b'250')),
                ('root_tweet', models.ForeignKey(blank=True, to='tweet.Tweet', null=True)),
            ],
            options={
                'verbose_name_plural': 'Tweet rilevati dallo stream di ATM',
            },
            bases=(models.Model,),
        ),
    ]
