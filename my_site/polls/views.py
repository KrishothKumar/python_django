from django.shortcuts import render

def index(request):
    return render(request,"index1.html", {"name" : "Pradeep"})

def add(request):
    var1 = int(request.POST["num1"])
    var2 = int(request.POST["num2"])
    res = var1 + var2

    return render(request,"result.html", {"res" : res})
