from django.http import HttpResponse
import music_selection.models as models
from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'music_selection/index.html')


def concert_list(request):
    return render(request, 'music_selection/concerts.html',
                  context={'concerts': models.Concert.objects.all().order_by('-year', 'concert_label')})


def concert_song_list(request, year, concert_label):
    concert = get_object_or_404(models.Concert, year=year, concert_label=concert_label)
    decisions = concert.suggestiondecision_set.select_related('suggestion').all()

    return render(request, 'music_selection/concert_song_list.html',
                  context={'concert': concert, 'decisions': decisions})


