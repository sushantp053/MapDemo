from django.contrib import admin
from django.urls import path, include
from home.views import *
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'natoshi', NatoshiViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('natoshi1/', NatoshiViewSet1.as_view()),

]
