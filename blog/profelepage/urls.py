from . import views
from django.urls import path

from .views import profile_page

urlpatterns = [
    path('', profile_page),
]
