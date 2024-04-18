from django.urls import path
from flights import views
urlpatterns = [
    path('', views.firstRoute,name="first-route"),
    
]