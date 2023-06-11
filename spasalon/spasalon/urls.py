from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import urls
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("homepage.urls")),
    path('feedback/', include("feedback.urls")),
    path("reception/", include("reception.urls")),
    path("reviews/", include("reviews.urls")),
    path("services/", include("services.urls")),
    path("specialists/", include("specialists.urls")),
    path("users/", include("users.urls")),
    path("users/", include(urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
