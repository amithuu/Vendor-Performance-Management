from django.urls import path
from user_vendor.views import *

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(),name='vendors_list_create'),
    path('api/vendors/<vendor_id>/', VendorRetrieveUpdateDestroyView.as_view(), name='vendor-retrieve-update-destroy'),
    
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-orders-list-create'),
    path('api/purchase_orders/<po_id>', PurchaseOrderRetrieveUpdateDestroyView.as_view(), name='purchase-orders-retrieve-update-destroy'),

    path('api/vendors/<vendor_id>/performance/', VendorPerformanceRetrieveView.as_view(), name='vendor-performance-retrieve'),
    path('api/purchase_orders/<pk>/acknowledge/', AcknowledgeUpdate.as_view()),
    
    path('login/', CustomAuthToken.as_view())
    
]
