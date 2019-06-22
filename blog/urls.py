from django.urls import path
from . import views 

urlpatterns = [
    
    path('texts/', views.texts, name='texts'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('guests/fromguestscreate/', views.fromguests_createform, name='fromguests_createform'),
    path('guests/fromguests/', views.fromguests, name='fromguests'),
    path('guests/', views.friends, name='guests'),
    path('guests/<int:guest_id>/', views.fromguests_detail, name='fromguests_detail'),


]