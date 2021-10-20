from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import index

urlpatterns = [
    path('off-limits/', admin.site.urls),
    path('', index, name='home'),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
