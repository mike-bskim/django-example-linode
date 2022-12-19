from django.urls import path
from . import views

# domain.com:8000/other
urlpatterns = [
    path('', views.simple_view, name='simple_view')
]