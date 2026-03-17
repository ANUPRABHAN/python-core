from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_student, name='view_student'),
]
