from django.shortcuts import render, HttpResponse
import urllib2
# Create your views here.
from django.db.models import Count
from django.http import JsonResponse
import json
from django.core.urlresolvers import reverse
from twython import Twython, TwythonError, TwythonStreamer
from django.conf import settings
from django.core.cache import cache
from textblob import TextBlob

def index(request):
     return render(request, 'index.html')

def graph(request):
     return render(request, 'graph.html')


def play_count_by_month(request):
     with open('data.json', 'r') as f:
          data=json.load(f)
          
     return JsonResponse(list(data), safe=False)

def sentiment(request):
    pos=0
    neg=0
    neu=0

    twitter = Twython(settings.TWITTER_CONSUMER_KEY,
                          settings.TWITTER_CONSUMER_SECRET,
                          settings.TWITTER_OAUTH_TOKEN,
                          settings.TWITTER_OAUTH_TOKEN_SECRET)
    search_results_l=[]
    test=[]
    max_x = 0
    
    results=twitter.search(q='football',count=200, pages=15, result_type='mixed')
    if results.get('statuses'):
        for result in results['statuses']:
            tweet = TextBlob(result["text"])
            if tweet.sentiment.polarity < 0:
                neg = neg+1
                test.append(tweet.sentiment.polarity)  
                for i in range(0,len(test)):
 		     temp_x = test[i]
 		     print temp_x
                     if temp_x >= max_x:
                         max_x = temp_x
                    
            elif tweet.sentiment.polarity == 0:
                neu = neu+1
            else:
                pos = pos+1
    print max_x
    return render(request,'sentiment.html',{'positive':pos,'negetive':neg,'neutral':neu})

def users(request):
     return render(request, 'users.html')

def search(request):
     return render(request, 'search.html')


def tiframe(request):
    link="http://topsy.com/analytics"
    response = urllib2.urlopen(link)
    the_page = response.read()
    return HttpResponse(the_page)
     


