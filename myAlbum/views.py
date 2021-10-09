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

def search_category(request):
    
    location=Location.get_locations()

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        search = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'search.html',{"message":message,"category": search,"location":location})
    else:
        return render(request, 'search.html')