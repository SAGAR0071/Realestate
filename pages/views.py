from django.shortcuts import render
from django.http import HttpResponse

import listings
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import bedroom_choice,price_choice,state_choices


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices':state_choices,
        'price_choice':price_choice,
        'bedroom_choice':bedroom_choice,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    # Get Realtor
    realtors = Realtor.objects.order_by('-hire_Date')
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context3 = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }

    return render(request, 'pages/about.html', context3)

# Create your views here.
