from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('add-bus/', views.add_bus, name='add_bus'),
    path('subtract-bus/', views.subtract_bus, name='subtract_bus'),

    path('add-coster/', views.add_coster, name='add_coster'),
    path('subtract-coster/', views.subtract_coster, name='subtract_coster'),

    path('add-taxi/', views.add_taxi, name='add_taxi'),
    path('subtract-taxi/', views.subtract_taxi, name='subtract_taxi'),

]