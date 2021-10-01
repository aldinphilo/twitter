from django.http.response import Http404, JsonResponse
from django.shortcuts import render

# Create your views here.
from .models import Tweets


def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_list_view(request, *args, **kwars):
    qs = Tweets.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    '''
    REST API View
    return json data
    '''
    status = 200
    data = {
        "id": tweet_id,
    }
    try:
        obj = Tweets.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404
    return JsonResponse(data, status=status)
