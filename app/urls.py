from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomePageView, ContactPageView, AboutPageView,
    VendorListView, VendorDetailView, VendorCreateView, VendorUpdateView, VendorDeleteView,
    DishListView, DishDetailView, DishCreateView, DishUpdateView, DishDeleteView,
    EventListView, EventDetailView, EventCreateView, EventUpdateView, EventDeleteView,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    ReservationListView, ReservationDetailView, ReservationCreateView, ReservationUpdateView, ReservationDeleteView,
    ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView
)

urlpatterns = [

    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('about/', AboutPageView.as_view(), name='about'),

    # Vendor Views
    path('vendors/', VendorListView.as_view(), name='vendor_list'),
    path('vendor/<int:pk>/', VendorDetailView.as_view(), name='vendor_detail'),
    path('vendor/create/', VendorCreateView.as_view(), name='vendor_create'),
    path('vendor/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor_update'),
    path('vendor/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor_delete'),

    # Dish Views
    path('dishes/', DishListView.as_view(), name='dish_list'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('dish/create/', DishCreateView.as_view(), name='dish_create'),
    path('dish/<int:pk>/update/', DishUpdateView.as_view(), name='dish_update'),
    path('dish/<int:pk>/delete/', DishDeleteView.as_view(), name='dish_delete'),

    # Event Views
    path('events/', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event/create/', EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event_update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

    # Post Views
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Reservation Views
    path('reservations/', ReservationListView.as_view(), name='reservation_list'),
    path('reservation/<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    path('reservation/create/', ReservationCreateView.as_view(), name='reservation_create'),
    path('reservation/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('reservation/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),

    # Review Views
    path('reviews/', ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review/create/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)