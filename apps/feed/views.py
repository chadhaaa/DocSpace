from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 

from .models import tweet
# Create your views here.

@login_required
def feed(request):
    userids = [request.user.id]

    for twee in request.user.userProfile.follows.all(): 
        userids.append(twee.user.id)

    tweets = tweet.objects.filter(created_by_id__in = userids)


    for twee in tweets: 
        likes = twee.likes.filter(created_by_id = request.user.id)

        if likes.count() > 0:
            twee.liked = True 
        else:
            twee.liked = False 

    return render(request, 'feed/feed.html', {'tw': tweets})

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0: 
        tweets = User.objects.filter(username__icontains = query)
        twe = tweet.objects.filter(body__icontains = query)
    else: 
        tweets = []
        twe = []
         
    
    context = {
        'query': query, 
        'tweets': tweets,
        'twe': twe
    }

    return render(request, 'feed/search.html', context)