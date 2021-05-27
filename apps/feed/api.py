import json 

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 

from .models import tweet, Like 

@login_required
def api_tweet(request):
    data = json.loads(request.body)
    body = data['body']

    Tweet = tweet.objects.create(body=body, created_by = request.user) 

    return JsonResponse({'success': True})

@login_required
def api_like(request): 
    data = json.loads(request.body)
    tweet_id = data['tweet_id']

    if not Like.objects.filter(tweet_id = tweet_id).filter(created_by = request.user).exists():
        like = Like.objects.create(tweet_id = tweet_id, created_by = request.user)

    return JsonResponse({'success': True})