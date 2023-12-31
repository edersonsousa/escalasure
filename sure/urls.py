"""sure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.views.generic import TemplateView
from app.views import (
    home,
    form,
    create,
    paineldeescalas,
    view,
    edit,
    update,
    delete,
    dashboard,
    json,
    dash,
    dash2,
    index,
)
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'home/',
        TemplateView.as_view(template_name='dashboard/home.html'),
        name='home',
    ),
    # path('home/', views.home, {'escala': 1}),
    # path('', TemplateView.as_view(template_name='account/login.html'), name='login'),
    path('', index, name='index'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('dashboard', dashboard, name='dashboard'),
    path('dash', dash, name='dash'),
    path('dash2', dash2, name='dash2'),
    path('json', json, name='json'),
    path('paineldeescalas', paineldeescalas, name='paineldeescalas'),
    path('accounts/', include('allauth.urls')),
]
