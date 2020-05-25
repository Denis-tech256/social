
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
#('accounts/', include('accounts.urls')),
path('accounts/', include('django.contrib.auth.urls')),
path('', include('core.urls')),
path('accounts/', include('accounts.urls')),
]
