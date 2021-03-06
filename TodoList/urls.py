from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('archive', views.archive, name='archive'),
    path('done/<id>', views.done, name='done'),
    path('undone/<id>', views.undone, name='undone'),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete, name='delete'),
]