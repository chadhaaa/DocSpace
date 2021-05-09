from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import tweet
# Create your views here.

@login_required
def feed(request):
    userids = [request.user.id]

    for twee in request.user.userProfile.follows.all(): 
        userids.append(twee.user.id)

    tweets = tweet.objects.filter(created_by_id__in = userids)
    return render(request, 'feed/feed.html', {'tw': tweets})