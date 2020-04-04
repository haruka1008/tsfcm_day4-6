from django.shortcuts import render
from django.views import generic

# Create your views here.

def Index(requests):
    return render(requests, 'diary/day_list.html')
