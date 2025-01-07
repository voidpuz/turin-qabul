from django.contrib import admin

from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("payment_type", "id", "status", "paid_at", "canceled_at")
    list_filter = ("payment_type", "status")
    search_fields = ("id",)
    list_per_page = 50
