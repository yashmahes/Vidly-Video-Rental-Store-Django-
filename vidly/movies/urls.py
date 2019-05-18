from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail'),
    path('add', views.add, name='add'),
    path('delete/<int:movie_id>', views.delete, name='delete'),
]
