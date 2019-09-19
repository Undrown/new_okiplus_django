from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.brends, name='Brendy'),
    path('<int:brend_id>/', views.brend, name='Brend'),
]