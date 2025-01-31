from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vendor, Dish, Event, Post, Reservation, Review
from django.http import HttpResponseForbidden

class HomePageView(TemplateView):
    template_name = 'app/home.html'


class ContactPageView(TemplateView):
    template_name = 'app/contact.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'








class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor/vendor_list.html'
    context_object_name = 'vendors'

class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'vendor/vendor_detail.html'
    context_object_name = 'vendor'


class VendorCreateView(CreateView):
    model = Vendor
    fields = ['image', 'name', 'description', 'location', 'contact_number']
    template_name = 'vendor/vendor_create.html'
    success_url = reverse_lazy('vendor_list')

    def form_valid(self, form):
        # Ensure only vendors can create vendors
        if self.request.user.role != 'vendor':
            return HttpResponseForbidden("Only vendors can create a vendor.")

        # Check if the user already has a vendor
        if Vendor.objects.filter(user=self.request.user).exists():
            return HttpResponseForbidden("You already have a vendor account.")

        form.instance.user = self.request.user  # Associate the logged-in user with the vendor
        return super().form_valid(form)

class VendorUpdateView(UpdateView):
    model = Vendor
    fields = ['image', 'name', 'description', 'location', 'contact_number']
    template_name = 'vendor/vendor_update.html'
    success_url = reverse_lazy('vendor_list')

class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'vendor/vendor_delete.html'
    success_url = reverse_lazy('vendor_list')



class DishListView(ListView):
    model = Dish
    template_name = 'dish/dish_list.html'
    context_object_name = 'dishes'

class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish/dish_detail.html'
    context_object_name = 'dish'


class DishCreateView(CreateView):
    model = Dish
    fields = ['name', 'description', 'price', 'image']
    template_name = 'dish/dish_create.html'
    success_url = reverse_lazy('dish_list')

    def form_valid(self, form):
        # Ensure only vendors can create dishes
        if self.request.user.role != 'vendor':
            return HttpResponseForbidden("Only vendors can create a dish.")

        form.instance.vendor = Vendor.objects.get(user=self.request.user)  # Link the dish to the vendor
        return super().form_valid(form)


class DishUpdateView(UpdateView):
    model = Dish
    fields = ['name', 'description', 'price', 'image']
    template_name = 'dish/dish_update.html'
    success_url = reverse_lazy('dish_list')

class DishDeleteView(DeleteView):
    model = Dish
    template_name = 'dish/dish_delete.html'
    success_url = reverse_lazy('dish_list')







class EventListView(ListView):
    model = Event
    template_name = 'event/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'event/event_detail.html'
    context_object_name = 'event'


class EventCreateView(CreateView):
    model = Event
    fields = ['title', 'date', 'location', 'description',]
    template_name = 'event/event_create.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        # Ensure only vendors can create events
        if self.request.user.role != 'vendor':
            return HttpResponseForbidden("Only vendors can create events.")

        return super().form_valid(form)


class EventUpdateView(UpdateView):
    model = Event
    fields = ['title', 'date', 'location', 'description', 'vendors']
    template_name = 'event/event_update.html'
    success_url = reverse_lazy('event_list')

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'event/event_delete.html'
    success_url = reverse_lazy('event_list')









class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        vendor = Vendor.objects.get(user=self.request.user)  # Get the Vendor associated with the user
        form.instance.user = vendor  # Assign Vendor to the user field
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'post/post_update.html'
    success_url = reverse_lazy('post_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('post_list')







class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservation/reservation_list.html'
    context_object_name = 'reservations'

class ReservationDetailView(DetailView):
    model = Reservation
    template_name = 'reservation/reservation_detail.html'
    context_object_name = 'reservation'

class ReservationCreateView(CreateView):
    model = Reservation
    fields = [ 'dish', 'event', 'quantity']
    template_name = 'reservation/reservation_create.html'
    success_url = reverse_lazy('reservation_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Associate the logged-in user with the reservation
        return super().form_valid(form)


class ReservationUpdateView(UpdateView):
    model = Reservation
    fields = ['dish', 'event', 'quantity']
    template_name = 'reservation/reservation_create.html'
    success_url = reverse_lazy('reservation_list')

class ReservationDeleteView(DeleteView):
    model = Reservation
    template_name = 'reservation/reservation_delete.html'
    success_url = reverse_lazy('reservation_list')







class ReviewListView(ListView):
    model = Review
    template_name = 'review/review_list.html'
    context_object_name = 'reviews'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review/review_detail.html'
    context_object_name = 'review'

class ReviewCreateView(CreateView):
    model = Review
    fields = [ 'dish', 'rating', 'comment']
    template_name = 'review/review_create.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Associate the logged-in user with the review
        return super().form_valid(form)


class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['rating', 'comment']
    template_name = 'review/review_update.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review/review_delete.html'
    success_url = reverse_lazy('review_list')
