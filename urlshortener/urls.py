from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('<str:slug>/', views.visit_url, name='visit_url'),
    path('db/clear/', views.clearDb, name='clear'),
]