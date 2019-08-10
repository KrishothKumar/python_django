from django.shortcuts import render
from .models import Destination

def index(request):
    dest = Destination.objects.all() # Select all fields in the Model(ORM) exactly Select * from table
    return render(request,"index.html", {"dests": dest})
