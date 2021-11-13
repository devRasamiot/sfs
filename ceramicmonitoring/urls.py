"""ceramicmonitoring URL Configuration

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

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.conf import settings
from django.conf.urls.static import static


root_address = 'management/api/'
urlpatterns = [
    path(root_address+'admin/', admin.site.urls),
    path(root_address+'', include('factory.urls')),
    path(root_address+'reports/', include('reports.urls')),
    # path('user/', include('users.urls')),
    # path('api/token/', obtain_jwt_token , name='token_obtain_pair'),
    # path('api/token/refresh/', refresh_jwt_token, name='token_refresh'),
    
    path(root_address+'user/', include('users.urls', namespace='users')),
    path(root_address+'auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
