from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)
        print(user)
        if user:
            auth.login(request, user)
            print(user)
            return redirect('/travel')
        else:
            messages.info(request, "Username or Password may incorrect")
            return redirect('/login')

    else:
        return render(request, 'login.html')


def register(request):

    if request.method == "GET":
        return render(request, 'register.html')
    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        e_mail = request.POST["e_mail"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Exists")
                return redirect('/register')
            elif User.objects.filter(email = e_mail).exists():
                messages.info(request, "E_mail Exists")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password = password1,email= e_mail,
                first_name= first_name, last_name=last_name)
                user.save()
                return redirect('/travel')
        else:
            messages.info(request, "password is not same")
            return redirect('/register')

def logout(request):
    auth.logout(request)
    return redirect('/travel')
