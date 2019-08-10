from django.contrib import admin
from .models import Question

# Assigning Question into Django Admin
admin.site.register(Question)
