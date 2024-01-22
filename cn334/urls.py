
from django.contrib import admin
from django.urls import path


from ecommerce import views as ecom_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce/', ecom_views.ecommerce_index_view),
    path('ecommerce/item/<item_id>', ecom_views.item_view),
    
    # HW3
    path('ecommerce/homepage', ecom_views.homepage_view),
    path('ecommerce/contacts', ecom_views.contacts_view),
    path('ecommerce/categories', ecom_views.categories_view),
    path('ecommerce/products', ecom_views.products_view),
    path('ecommerce/checkout', ecom_views.checkout_view)
]