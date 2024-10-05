from rest_framework.routers import DefaultRouter
from .views import Driverview
from django.urls import path , include

router = DefaultRouter()
router.register(r'drivers', Driverview)

urlpatterns = [
path('' ,include(router.urls))
]

