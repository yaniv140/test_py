from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from users.forms import UserLoginForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            session_key = request.session.session_key

            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Ви увійшли в аккаунт")

                if session_key:
                    Cart.objects.filter(session_key=session_key).update(user=user)

                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                    
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()

    context = {
        'title': 'Euggen - Авторизація',
        'form': form
    }
    return render(request, 'users/login.html', context)




def registration(request):
    context={
        'title': 'Euggen - Авторизация',
    }
    return render(request, 'users/registration.html', context)




def profile(request):
    context={
        'title': 'Euggen - Авторизация',
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    context={
        'title': 'Euggen - Авторизация',
    }
    return render(request, 'users/logout.html', context)


