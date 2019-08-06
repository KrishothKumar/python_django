from rest_framework import routers
from .api import UserViewsets
from django.urls import include


router = routers.DefaultRouter()
router.register(r'input', UserViewsets, 'datainput')

urlpatterns = router.urls





















# urlpatterns = [
#     url(r'^', include(router.urls)),
# ]
