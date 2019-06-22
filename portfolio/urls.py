from django.urls import path
from . import views
   
urlpatterns = [
   
    path('photos/', views.photos, name='photos'),
    path('dogs/', views.dogs, name='dogs'),
    path('about/', views.about, name='about'),

]