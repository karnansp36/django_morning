from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import User_data
def home(request):
    return HttpResponse("Hello, welcome to the User Authentication App!")

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        if username == "" and password =="":
            HttpResponse('username is empty')
        
        else:
            try:
                user = User_data(username=username, email=email, password=password, phone=phone)
                user.save()
            except:
                HttpResponse('error in save')
    return render(request, 'userdata.html' )

def user_view(request):
    users = User_data.objects.all()
    return render(request, "userview.html", {'userdata':users})
