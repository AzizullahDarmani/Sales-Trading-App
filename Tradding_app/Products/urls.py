from django.urls import path
from .views import add_product, add_category, product_list, delete_product
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('add/', add_product, name='add_product'),
    path('list/', product_list, name='product_list'),
    path('add-category/', add_category, name='add_category'), 
    path('delete-product/<int:id>/', delete_product, name='delete_product' ),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)