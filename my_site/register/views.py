# "User" is default User-Module and auth is function used by User class to
#  lognin,logout and authenticate
from django.contrib.auth.models import User, auth
from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # This is user validate correct user is login or not
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request, user)
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
            # User.objects.filter is used to find specific field in the Model or ORM or Table
            if User.objects.filter(username = username).exists():
                messages.info(request, "Username Exists")
                return redirect('/register')
            elif User.objects.filter(email = e_mail).exists():
                messages.info(request, "E_mail Exists")
                return redirect('/register')
            else:
                # User.objects.create_user is creates User field in the Model or ORM or Table
                user = User.objects.create_user(username=username, password = password1,email= e_mail,
                first_name= first_name, last_name=last_name)
                user.save()
                return redirect('/travel')
        else:
            messages.info(request, "password is not same")
            return redirect('/register')

def logout(request):
    # This is used to clear the sessions or Make as logout
    auth.logout(request)
    return redirect('/travel')
