from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (HomePageView,
                    AboutPageView,
                    ContactPageView,
                    VendorListView,
                    VendorDetailView,
                    VendorCreateView,
                    VendorUpdateView,
                    VendorDeleteView,
                    ReservationCreateView)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('vendor/', VendorListView.as_view(), name='vendor'),
    path('vendor/<int:pk>/', VendorDetailView.as_view(), name='vendor_detail'),
    path('vendor/add/', VendorCreateView.as_view(), name='vendor_create'),
    path('vendor/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor_update'),
    path('vendor/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor_delete'),

    path('reserve/<int:dish_pk>/', ReservationCreateView.as_view(), name='reserve_dish'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)