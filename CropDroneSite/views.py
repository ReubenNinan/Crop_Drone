from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def home(request):
    #return render(request, 'home.html', {'name': 'Reuben'}); 
    # #curly bracket references dyanmic information and will be called in HTML file

def index (request):
    return render(request, 'index.html')