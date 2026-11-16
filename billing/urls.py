from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('client/new/', views.ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),
    
    path('invoice/', views.InvoiceListView.as_view(), name='invoice_list'),
    path('invoice/<int:pk>/', views.InvoiceDetailView.as_view(), name='invoice_detail'),
    path('invoice/new/', views.InvoiceCreateView.as_view(), name='invoice_create'),
    
    path('taxrate/', views.TaxRateListView.as_view(), name='taxrate_list'),
    path('taxrate/new/', views.TaxRateCreateView.as_view(), name='taxrate_create'),
    
    path('transaction/', views.TransactionListView.as_view(), name='transaction_list'),
    path('transaction/new/', views.TransactionCreateView.as_view(), name='transaction_create'),
]