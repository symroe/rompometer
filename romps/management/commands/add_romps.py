import sys
import re
import datetime
import time
# import dateutil

import feedparser

from django.core.management.base import BaseCommand, CommandError

from romps.models import Romp

class Command(BaseCommand):
    
    def handle(self, **options):
        urls = (
            ('mail','http://www.dailymail.co.uk/home/search.rss?searchPhrase=romp'),
            ('sun','http://www.thesun.co.uk/search/customRSSsearch.do?view=internal&query=romp'),
        )
        
        for paper, url in urls:
            feed = feedparser.parse(url)
            for item in feed['entries']:

                django_timestamp = datetime.datetime.fromtimestamp(time.mktime(item.updated_parsed))
                date = django_timestamp

                try:
                    R = Romp.objects.get(link=item.link)
                except:
                    R = Romp(link=item.link)

                R.title = item['title']
                R.paper = paper
                R.date = date
                R.save()