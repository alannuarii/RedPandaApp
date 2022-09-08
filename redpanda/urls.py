from baton.autodiscover import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view
from redpanda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    path('', views.home, name='home'),
    path('delete/<int:id>', views.delete_cost, name='delete_cost'),
    path('auth/sign-in', views.sign_in, name='sign_in'),
    path('sign-out', views.sign_out, name='sign_out'),
    path('auth/change-password', auth_view.PasswordChangeView.as_view(
        template_name='pages/auth/change-password.html',
        success_url='/'
    ), name='change_password'),
    path('feeder/forecast', views.forecast_feeder, name='forecast_feeder'),
    path('feeder/data', views.data_feeder, name='data_feeder'),
    path('pemeliharaan/rencana', views.rencana_har, name='rencana_har'),
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)