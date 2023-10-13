"""
URL configuration for myFirstApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from my_first_app import views

urlpatterns = [
    path('', views.hello_user_view, name='hello_user'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('data/<str:model>/', views.FBA_LIST),
    path('generate_sudoku/<int:N>/<int:K>/', views.generate_sudoku),
    path('generate_equation/<str:level>/<int:num_parameters>/<int:num_digits>/', views.generate_equation),
    path('validate_answer/', views.validate_answer),
    path('sodokuSolver/', views.sudokuSolver)
]
