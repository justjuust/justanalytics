"""
URL configuration for justanalytics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from onepager import views
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    "static": views.StaticViewSitemap,  # Sitemap for static pages
}

urlpatterns = [
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('animacel', views.animacel_view, name='case_study_animacel'),
    path('veterinary', views.veterinary_view, name='veterinary'),
    path('contact/', views.contact_view, name='contact_view'),  # Add your URL here
]
