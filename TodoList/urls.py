from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('done/<id>', views.done, name='done'),
    path('undone/<id>', views.undone, name='undone'),
    path('edit/<id>', views.edit, name='edit'),
]