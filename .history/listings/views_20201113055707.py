from django.http import request
from django.shortcuts import render

from .models import Listing
# Create your views here.


def index(request):
    listing = Listing.object.all()
    context = {

    }
    return render(request, 'listings/listings.html')


def listing(request):
    return render(request, 'listings/listing.html')


def search(request):
    return render(request, 'listings/search.html')
