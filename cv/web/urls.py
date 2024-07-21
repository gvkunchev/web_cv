from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_bg),
    path('bg', views.index_bg),
    path('en', views.index_en),
]
