from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('display/<int:superhero_id>/', views.detail, name='detail')
]
