from django.contrib import admin
from django.urls import path, include
from core.views import landing_page   # 👈 import landing
from django.conf import settings             # ADD THIS
from django.conf.urls.static import static   # ADD THIS

urlpatterns = [
    path("admin/", admin.site.urls),

    path('', landing_page, name='landing'),   # ✅ "/" = landing page

    path('', include('dashboard.urls')),  # ✅ handles /home/

    path('accounts/', include('accounts.urls')),
    path('mentorship/', include('mentorship.urls')),
    path('collaboration/', include('collaboration.urls')),
    path('marketplace/', include('marketplace.urls')),
    path('resources/', include('resources.urls')),
    path('lostfound/', include('lostfound.urls')),
        # admin panel
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)