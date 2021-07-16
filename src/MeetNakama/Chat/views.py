from django.shortcuts import render

# Create your views here.
def Signup(request):
    return render(request, 'signup.html')

#def Login(request):
#    return render(request, 'login.html')

def PasswordReset(request):
    return render(request, 'passwordReset.html')

def Home(request):
    return render(request, 'home.html')
