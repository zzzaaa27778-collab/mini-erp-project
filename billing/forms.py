from django import forms
from .models import Client, Invoice, InvoiceItem, TaxRate, Transaction

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['invoice', 'description', 'quantity', 'price', 'taxrate']

class TaxRateForm(forms.ModelForm):
    class Meta:
        model = TaxRate
        fields = ['name', 'rate']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['invoice', 'amount', 'date']