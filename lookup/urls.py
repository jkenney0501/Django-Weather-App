from django.urls import path
from . import views

urlpatterns = [
#where does this point? views.home, we just created this in views
    path('', views.home, name="home"), 

    path('about.html', views.about, name="about"),


    
]