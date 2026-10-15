from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def start(request):
    lst_team = Team.objects.all()
    lst_menues = Menue.objects.all()

    content = {
        'teams': lst_team,
        'menues': lst_menues,
    }

    return render(request, "bestellung/start.html", content) 

