from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView , DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Vendor, Dish, Reservation


class HomePageView(TemplateView):
    template_name = 'app/home.html'


class ContactPageView(TemplateView):
    template_name = 'app/contact.html'


class AboutPageView(TemplateView):
    template_name = 'app/about.html'


# Vendor List View
class VendorListView(ListView):
    model = Vendor
    template_name = 'app/vendor_list.html'
    context_object_name = 'vendors'


class VendorCreateView(CreateView):
    model = Vendor
    fields = ['image', 'name', 'description', 'location', 'contact_number']
    template_name = 'app/vendor_create.html'

    def form_valid(self, form):
        # Check if the user already has a Vendor profile
        if Vendor.objects.filter(user=self.request.user).exists():
            messages.error(self.request, "You already have a vendor profile.")
            return HttpResponseRedirect(reverse_lazy('vendor'))  # Redirect to a relevant page

        # Set the user as the current logged-in user
        form.instance.user = self.request.user
        return super().form_valid(form)

# Vendor Detail View with Dishes
class VendorDetailView(DetailView):
    model = Vendor
    template_name = 'app/vendor_detail.html'
    context_object_name = 'vend'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dishes'] = Dish.objects.filter(vendor=self.object)
        return context

class VendorUpdateView(UpdateView):
    model = Vendor
    fields = '__all__'
    context_object_name = 'vend'
    template_name = 'app/vendor_update.html'

class VendorDeleteView(DeleteView):
    model = Vendor
    template_name = 'app/vendor_delete.html'
    success_url = reverse_lazy('vendor')  # This redirects after successful deletion

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vend'] = self.object  # Make sure the vend object is passed correctly
        return context


class ReservationCreateView(CreateView):
    model = Reservation
    fields = ['quantity']
    template_name = 'reservation_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.dish = get_object_or_404(Dish, pk=self.kwargs['dish_pk'])

        existing_reservation = Reservation.objects.filter(
            user=self.request.user, dish=form.instance.dish
        ).first()
        if existing_reservation:
            return redirect('vendor_detail', pk=form.instance.dish.vendor.pk)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('vendor_detail', kwargs={'pk': self.object.dish.vendor.pk})