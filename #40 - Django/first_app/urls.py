from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num1>', views.course_number_view, name='course_number'),
    path('<str:course_name>/', views.course, name='course'),
    path('multiply/<int:num1>/<int:num2>/', views.multiply_view, name='multiply'),
]