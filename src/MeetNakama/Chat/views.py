from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Users.forms import CustomUserCreationForm

# Create your views here.
def Signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/home")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {"form":form})

@login_required
def Home(request):
    return render(request, 'home.html')

@login_required
def Settings(request):
    if request.method == "POST":
        pass
    return render(request, 'settings.html')

@login_required
def Chat(request):
    return render(request, 'chat.html')
