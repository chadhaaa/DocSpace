import json 

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required 

from .models import tweet

@login_required

def api_tweet(request):
    data = json.loads(request.body)
    body = data['body']

    tweet = tweet.objects.create(body=body, created_by = request.user) 

    return JsonResponse({'success': True})
