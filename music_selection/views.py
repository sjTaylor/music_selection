from django.http import HttpResponse
from .models import Section, Concert
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'music_selection/index.html')


def concert_list(request):
    return render(request, 'music_selection/concerts.html',
                  context={'concerts': Concert.objects.all().order_by('-year', 'concert_label')})




