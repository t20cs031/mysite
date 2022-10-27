'''
Created on 2022/10/28

@author: t20cs031
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]