from django.contrib import admin
from .models import Booking, Payment

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'service', 'booking_time', 'status')
    list_filter = ('status', 'booking_time')
    search_fields = ('user__email', 'service__name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'amount', 'status', 'payment_date')
    list_filter = ('status', 'payment_method')
    search_fields = ('booking__id', 'transaction_id')