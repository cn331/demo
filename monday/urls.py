from django.urls import path

from . import views

app_name = 'monday'
urlpatterns = [
    path('', views.index, name='index')
]
