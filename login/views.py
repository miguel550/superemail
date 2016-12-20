from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    # import pdb; pdb.set_trace()
    if not request.user.is_authenticated:
        return render(request, 'login/index.html')
    else:
        return render(request, 'login/index.html', {'user': request.user})


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # import pdb; pdb.set_trace()
        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request, user)
            print("Authenticated!")
            return redirect('index')
        else:
            print("Not authenticated!")
            return redirect('index')
