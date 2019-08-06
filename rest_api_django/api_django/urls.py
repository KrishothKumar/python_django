from rest_framework import routers
from .api import UserViewsets
from django.urls import include

router = routers.DefaultRouter() # This basicaly routs paths with Api roots
router.register(r'input', UserViewsets, 'datainput') # Assigning url for routers and fuctions to execute

urlpatterns = router.urls # Mention that routers url in urlpatterns to work path
