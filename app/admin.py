from django.contrib import admin
from .models import Review, Profile, Vendor , Dish, Event, Post

admin.site.register(Profile)
admin.site.register(Vendor)
admin.site.register(Dish)
admin.site.register(Event)
admin.site.register(Post)
admin.site.register(Review)
