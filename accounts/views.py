from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from _typeshed import ReadableBuffer
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['Password']

        user = auth.authenticate(username=username, password=Password)

        if user is not None:
            auth.login(request, user)
            return redirect("/") #calling the homepage
        else: 
            messages.error(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')



    


def register(request):

    if request.method == 'POST': #creating parameters for new object 'user'
        username = request.POST['username']
        email = request.POST['email']
        Password_1 = request.POST['Password_1']
        Password_2 = request.POST['Password_2']

        #!time to create checks for password 1 and 2 AND to check if the username has already been used
        if Password_1 == Password_2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "username taken")
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info((request, "Account already exists with email"))
                return redirect('register')

            else:
                user = User.objects.create_user(username = username, password = Password_1, email = email) #created object for every single new user
                user.save();
                print("Welcome to the Matrix")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')

    # return redirect('/')

    return render(request, 'register.html');

