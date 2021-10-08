from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404
from myAlbum.models import Category, Location, Image

# Create your views here.
def homepage(request):
    """
    View function to render homepage
    """
    images = Image.objects.all()
    location=Location.get_locations()

    return render(request, 'all-gallery/album-homepage.html', {"images":images,"location":location})