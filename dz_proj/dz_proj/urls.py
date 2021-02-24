from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from docs.views import MainView, file_upload_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main-view'),
    path('upload/', file_upload_view, name='upload-view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)