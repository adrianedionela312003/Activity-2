from django.urls import path
from .views import homepageview, aboutpageview, contactpageview

urlpatterns = [
    path('',homepageview.as_view(),name='home'),
    path('/contact', contactpageview.as_view(), name='contact'),
    path('/about', aboutpageview.as_view(), name='about')

]