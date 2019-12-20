from django.shortcuts import render
from gameplay.models import Game
# Create your views here.


def home(request):
    view_data = {'ngames': Game.objects.count()}
    return render(request, "player/home.html", view_data)
