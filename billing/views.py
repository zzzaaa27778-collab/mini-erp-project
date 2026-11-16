from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Client, Invoice, InvoiceItem, TaxRate, Transaction

class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'

class ClientCreateView(CreateView):
    model = Client
    fields = ['name', 'email', 'phone']
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['name', 'email', 'phone']
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

# (ويمكنك إضافة بقية الـ Class-Based Views الخاصة بالفواتير والضرائب بنفس النمط الكلاسيكي السليم الذي بناه المبرمج).