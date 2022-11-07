from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.PostView.as_view()),
    path("<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
