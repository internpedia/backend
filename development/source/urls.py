"""
URL configuration for source project.

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
from rest_framework import routers
from internpedia import views
from internpedia.views import InternshipSearchView, CompanyDetailView


router = routers.DefaultRouter()
router.register(r'Internship', views.InternshipView, 'Internship')
router.register(r'Company', views.CompanyView, 'Company')
router.register(r'Review', views.ReviewView, 'Review')
router.register(r'Vote', views.VoteView, 'Vote')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/internships/search/', InternshipSearchView.as_view(), name='internship_search'),
    path('api/companies/<int:company_id>/', CompanyDetailView.as_view(), name='company_detail')
]
