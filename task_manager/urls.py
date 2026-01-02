from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('api-auth/', include('rest_framework.urls')),  # for login/logout in browsable API
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.api_urls')),  # ✅ DRF API
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # Django admin
    path('api/', include('tasks.api_urls')),  # Your API endpoints
]
