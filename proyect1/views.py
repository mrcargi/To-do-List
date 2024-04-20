from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from TDL.models import Task

@login_required
def home(request):
    activepage = "home"
    return render(
        request,
        'home.html',
        {'activepage':activepage},
        
    )

def exit(request):
    logout(request)
    return redirect('login')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data = request.POST)   
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username = user_creation_form.cleaned_data['username'], 
                                password = user_creation_form.cleaned_data['password1'])
            login(request,user)

            return redirect('home') 
        print(user_creation_form.is_valid())
    
    return render(request, 'registration/register.html',data)
