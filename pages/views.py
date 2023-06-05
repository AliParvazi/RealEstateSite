from django.shortcuts import render
from django.http import HttpResponse
from listings.models import listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings' : listings,
        'prices' : price_choices,
        'bedrooms' : bedroom_choices,
        'states' : state_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realotrs = Realtor.objects.order_by('-name')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)
    context = {
        'realtors' : realotrs,
        'mvp_realtors' : mvp_realtors
    }
    return render(request, 'pages/about.html', context)
    