from django.shortcuts import render
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

def Home(request):
    return render(request, 'home.html')
