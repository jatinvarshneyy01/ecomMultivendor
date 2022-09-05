from django.urls import path
from . import views

urlpatterns = [
    path('vendor/', views.VendorList.as_view(), name='vendorlist')
]
