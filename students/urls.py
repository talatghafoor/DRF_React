from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentlist, name='list'),
    path('view/<int:pk>', views.studentview, name='view'),
    path('create', views.studentcreate, name='create'),
    path('update/<int:pk>', views.studentupdate, name='update'),
    path('delete/<int:pk>', views.studentdelete, name='delete'),
]

