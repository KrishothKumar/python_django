from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
path('', TemplateView.as_view(template_name='base.html') , name= "home"),
path('login', views.login , name= "login"),
path('register', views.register , name= "register"),
path('logout', views.logout , name= "logout")
]
