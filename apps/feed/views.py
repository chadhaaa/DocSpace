from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

from .models import Tweet
# Create your views here.

@login_required
def feed(request):
    userids = [request.user.id]

    for twee in request.user.userprofile.follows.all(): 
        userids.append(twee.user.id)

    tweets = Tweet.objects.filter(created_by_id__in = userids)


    for tweet in tweets: 
        likes = tweet.likes.filter(created_by_id = request.user.id)

        if likes.count() > 0:
            tweet.liked = True 
        else:
            tweet.liked = False 

    return render(request, 'feed/feed.html', {'tweets': tweets})

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0: 
        tweets = User.objects.filter(username__icontains = query)
        twe = Tweet.objects.filter(body__icontains = query)
    else: 
        tweets = []
        twe = []
         
    
    context = {
        'query': query, 
        'tweets': tweets,
        'twe': twe
    }

    return render(request, 'feed/search.html', context)

def searchbytweetbody(request):
		tweet = request.GET.get['tweet']
		if tweet is None :
			tweets = []
		else:
			tweets= Tweet.objects.filter(body = tweet)
		
		return render(request,'feed/search.html',tweets)