from django.contrib import admin
from .models import Destinations, CustomUser, Trip

# Register your models here.
@admin.register(Destinations)
class DestinationsAdmin(admin.ModelAdmin):

    list_display = ['name', 'price', 'image', 'description', 'spatial_offer', 'created_at']

    def image(self, obj):
        return obj.img.url
    
    def description(self, obj):
        return obj.desc[:20]

    def spatial_offer(self, obj):
        return obj.offer

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    
    list_display = ['name', 'email', 'created_at']

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

        list_display = ['city', 'departure', 'arrival', 'budget', 'created_at']