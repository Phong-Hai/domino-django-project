from django.urls import path
from domino import views

urlpatterns = [
    path("",views.home, name="/"),
path('', include('domino_project.urls')),
    path('menu/', include('menu.urls')),
]
# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

]


