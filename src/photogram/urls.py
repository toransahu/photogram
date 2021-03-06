"""photogram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from rest_framework.documentation import include_docs_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("v1/auth/", include("djoser.urls")),
    path("v1/auth/", include("djoser.urls.authtoken")),
    path("v1/admin/", admin.site.urls),
    path(
        "",
        include_docs_urls(
            title="PhotoGram API",
            authentication_classes=[],
            permission_classes=[],
            description="Find all the PhotoGram API endpoints here",
        ),
    ),
    path("v1/photo/", include("hub.urls", namespace="hub-v1")),
]

# Media URLs
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
