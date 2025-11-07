from . import views
from django.urls import path

urlpatterns = [
    path('', views.text),
    path('superkrutoyurl/', views.text2)
]
