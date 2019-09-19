from django.urls import path

from page import views

urlpatterns = [
    path('', views.index, name='flatpage'),
    path('<page_name>/', views.page, name='flatpages'),
]