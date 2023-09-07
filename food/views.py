from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):
    goods = Good.objects.all()
    return render(request, 'food/index.html', {'goods': goods})


def about(request):
    return render(request, 'food/about.html')



