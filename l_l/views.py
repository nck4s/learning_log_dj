from django.shortcuts import render
from .models import Topic


def index(request):
    return render(request, 'index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)