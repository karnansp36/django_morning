from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return render(request, "index.html")

def about_view(reqeust):
    return render(reqeust, 'pages/about.html')