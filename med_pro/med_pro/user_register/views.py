from django.shortcuts import render,redirect
from .models import Register
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import Register

def register(request):

    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        store_name= request.POST["store_name"]
        address = request.POST["address"]
        gst_no = request.POST["gst_no"]
        telephone = request.POST["telephone"]
        city = request.POST["city"]
        state = request.POST["state"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if (password1 == password2):
            if Register.objects.filter(email = email).exists():
                messages.info(request, "E_mail Id already exists")
                return redirect('/register')

            else:
                save = Register(first_name = first_name, last_name = last_name, email = email, store_name = store_name, address = address,
                                gst_no = gst_no, telephone = telephone, city = city, state = state, password = password1)
                save.save()
                messages.info(request, "User Created successfully")
                return redirect('/register')
        else:
            messages.info(request, "Password is not mathching")
            return redirect('/register')
    else:

        return render(request,'register.html')


def login(request):

    if request.method == "POST":

        e_mail=request.POST["email"]
        password=request.POST["password"]
        user = auth.authenticate(username=e_mail, password=password)
        print(user)
        if user:
            print(user)
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username or Password may incorrect")
            return redirect('/login')

    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
