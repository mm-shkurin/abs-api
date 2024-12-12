
from auto.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/autodelete/<int:pk>', AutoAPIDestroy.as_view(), name='auto-destroy'),  # Изменено на AutoListView
    path('api/v1/autolist/', AutoAPIList.as_view(), name='auto-list'),  
     path('api/v1/categories/', CategoryViews.as_view(), name='auto-list'), 
    path('api/v1/autolist/<int:pk>/', AutoDetailView.as_view(), name='auto-detail'),
    # Авторизация
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Для отдачи статических файлов в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)