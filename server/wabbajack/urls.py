"""
URL configuration for wabbajack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from home import views as home_views
from taxes import views as tax_views
from taxes.views import (
    StateListView,
    StateDetailView,
    TownListView,
    TownDetailView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Homepage
    path('', home_views.index, name='index'),

    # Taxes URLs
    # States
    path('states/', StateListView.as_view(), name='state-list'),
    path('states/<int:pk>/', StateDetailView.as_view(), name='state-detail'),
    # Towns
    path('towns/', TownListView.as_view(), name='town-list'),
    path('towns/<int:pk>/', TownDetailView.as_view(), name='town-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
