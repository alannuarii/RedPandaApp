from baton.autodiscover import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from redpanda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)