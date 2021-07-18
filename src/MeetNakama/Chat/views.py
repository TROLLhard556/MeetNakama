from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json
from Users.forms import CustomUserCreationForm


# Create your views here.
def Signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/chat/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {"form":form})

@login_required
def Home(request):
    return render(request, 'home.html', {'name': request.user.first_name})

@login_required
def Settings(request):
    if request.method == "POST":
        pass
    return render(request, 'settings.html')

@login_required
def Chat(request, chatID):
    return render(request, 'chat.html', {
        'chatID': mark_safe(json.dumps(chatID)),
        'name': mark_safe(json.dumps(request.user.first_name))
    })
