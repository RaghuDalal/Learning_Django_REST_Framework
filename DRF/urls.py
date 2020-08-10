from django.urls import path
from DRF import views

urlpatterns = [
    path('emps/', views.employeeView),
]
