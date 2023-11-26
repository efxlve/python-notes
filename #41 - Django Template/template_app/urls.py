from django.urls import path
from . import views

# app_name register, to use the namespace in the html files {% url 'template_app:index' %}
app_name = 'template_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('weather/', views.weather_view, name='weatherview'),
]