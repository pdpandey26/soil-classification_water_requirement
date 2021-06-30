from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from water_r import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('result/',views.result,name='result'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=staticfiles_urlpatterns()