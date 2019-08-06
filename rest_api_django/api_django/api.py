import json
from .models import UserApis
from .serializers import UserSerializers
from django.shortcuts import redirect
from rest_framework import (viewsets, renderers, permissions)
from django.http import HttpResponse

# Creating viewsets and inheriting UserApis and UserSerializers class from .model.py and .serializers.py (3rd)
class UserViewsets(viewsets.ModelViewSet):
    queryset = UserApis.objects.all()
    permission_classes = [
                        permissions.AllowAny
                       ]
    serializer_class= UserSerializers

    def get_queryset(self):
        if self.request.method == "POST":
            return redirect("/admin/")
        elif self.request.method == "GET":
            content = {}
            return HttpResponse(json.dumps(content), content_type='application/json')


# 'user_count': '2'
