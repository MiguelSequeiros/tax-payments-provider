from django.contrib import admin
from .models import Payable, Transaction

# Register your models here.

@admin.register(Payable)
class PayableAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'description', 'deadline', 'amount', 'state', )


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('barcode', 'payable', 'amount', 'date')