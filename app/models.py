from django.db import models
from django.urls import reverse
from django.conf import settings






class Vendor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('vendor_detail', kwargs={'pk': self.pk})


class Dish(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='dishes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='dishes/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dish_detail', kwargs={'pk': self.pk})



class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    vendors = models.ManyToManyField(Vendor, related_name='events')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})



class Post(models.Model):
    user = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.dish

    def get_absolute_url(self):
        return reverse('reservation_detail', kwargs={'pk': self.pk})


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, related_name='reviews', on_delete=models.CASCADE)
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rating


    def get_absolute_url(self):
        return reverse('review_detail', kwargs={'pk': self.pk})
