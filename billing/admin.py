from django.contrib import admin
from .models import Client, TaxRate, Invoice, InvoiceItem, Transaction

admin.site.register(Client)
admin.site.register(TaxRate)
admin.site.register(Invoice)
admin.site.register(InvoiceItem)
admin.site.register(Transaction)
# Register your models here.
