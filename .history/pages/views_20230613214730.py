from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing


def index(request):
    listings = Listing.order_by('-list_date').filter(is_published=True)
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')