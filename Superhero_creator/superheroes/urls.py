from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('display/<int:superhero_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create_superhero'),
    path('update/<int:superhero_id>/', views.update, name='update_superhero'),
    path('delete/<int:superhero_id>/', views.delete, name="delete")
]
