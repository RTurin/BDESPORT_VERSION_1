from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('DOTA2_APP.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = "BDESPORT.views.page_not_found_view"
