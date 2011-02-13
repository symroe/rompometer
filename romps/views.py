from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from django.db.models import Count

from models import Romp

def home(request):
    
    latest = Romp.objects.all().values('date').annotate(count=Count('pk')).order_by('-date')
    latest_count = len(latest)

    today = latest[0]
    yesterday = latest[1]
    
    today_romps = Romp.objects.filter(date=today['date'])
    yesterday_romps = Romp.objects.filter(date=yesterday['date'])
    
    return render_to_response(
        'home.html', 
        {
            'latest' : latest,
            'latest_count' : latest_count,
            'today' : today,
            'yesterday' : yesterday,
            'today_romps' : today_romps,
            'yesterday_romps' : yesterday_romps,
        },
        context_instance=RequestContext(request)
    )  
