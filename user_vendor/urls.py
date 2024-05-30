from django.urls import path
from user_vendor.views import *

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(),name='vendors_list_create'),
    path('api/vendors/<vendor_id>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),

]
