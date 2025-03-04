
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('User.urls')), 
    path('product/', include('Products.urls')), 
    path('sales/', include('Sales.urls')),
    path('tradings/', include('Trading.urls')), 
]


# to fectch back the images uploaded the following has to be written in the main "urls.py" file of the main directory of project. 
if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
