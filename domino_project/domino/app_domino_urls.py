from django.urls import path
from domino import views

urlpatterns = [
    path("",views.home, name="/"),
]


