import json 
import re

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User

from apps.notification.utilities import create_notification

from .models import Tweet, Like 

@login_required
def api_tweet(request):
    data = json.loads(request.body)
    body = data['body']

    tweet = Tweet.objects.create(body=body, created_by = request.user) 
    results = re.findall("(^|[^@\w])@(\w{1,20})", body)

    for result in results: 
        result = result[1]

        print (result)

        if User.objects.filter(username = result).exists() and result != request.user.username: 
            create_notification(request, User.objects.get(username = result), 'mention')

    return JsonResponse({'success': True})

@login_required
def api_like(request): 
    data = json.loads(request.body)
    tweet_id = data['tweet_id']

    if not Like.objects.filter(tweet_id = tweet_id).filter(created_by = request.user).exists():
        like = Like.objects.create(tweet_id = tweet_id, created_by = request.user)
        tweeet = Tweet.objects.get(pk = tweet_id)
        create_notification(request, tweeet.created_by, 'like')

    return JsonResponse({'success': True})