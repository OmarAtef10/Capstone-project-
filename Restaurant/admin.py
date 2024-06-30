from django.contrib import admin
from .models import Booking, Menu


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_guests', 'booking_date')
    search_fields = ('name', 'booking_date')
    list_filter = ('booking_date',)
    date_hierarchy = 'booking_date'


admin.site.register(Booking, BookingAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'inventory')
    search_fields = ('title', 'price')
    list_filter = ('price',)


admin.site.register(Menu, MenuAdmin)
