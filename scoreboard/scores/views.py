from django.shortcuts import redirect, render
from time import sleep

from .models import Score

def home(request):
    scores = Score.objects.order_by('score')
    return render(request, 'scores/home.html', {'scores':scores})

def new_score(request):
    return render(request, 'scores/new_score.html')

def submission(request):
    name = request.GET['name']
    score = request.GET['score']
    return render(request, 'scores/submission.html', {'name':name,'score':score})

def rolled(request):
    return render(request, 'scores/rolled.html')

def yw(request):
    return render(request, 'scores/yw.html')


# Create your views here.
