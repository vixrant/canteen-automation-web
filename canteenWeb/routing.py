# Django channels routing

from django.urls import path
from . import consumers

websocket_urlpatterns = [path("ws/admin/", consumers.CanteenWebConsumer)]
