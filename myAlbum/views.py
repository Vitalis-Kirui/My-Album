from django.shortcuts import render, redirect
from django.http  import HttpResponse,Http404

# Create your views here.
def homepage(request):
    """
    View function to render homepage
    """
    return render(request, 'all-gallery/album-homepage.html')