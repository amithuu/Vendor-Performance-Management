from django.shortcuts import render
from user_vendor.serializers import *
from user_vendor.models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.


# class VendorListView(generics.ListAPIView):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer
#     # permission_classes = [IsAuthenticated]

#     def list(self, request, *args, **kwargs):
#         try:
#             queryset = self.get_queryset()
#             serializer = self.get_serializer(queryset, many=True)

#             if not queryset.exists():
#                 return Response({"message": "No vendors found"}, status=status.HTTP_404_NOT_FOUND)

#             return Response({'data':serializer.data, 'success':True},status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'Error':str(e)})
        
    
class VendorListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)

            if not queryset.exists():
                return Response({"message": "No vendors found"}, status=status.HTTP_404_NOT_FOUND)

            return Response({'data':serializer.data, 'success':True},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'Error':str(e)})
    
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'data':serializer.data, 'success':True},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'Error':str(e)})
        
    
class VendorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_url_kwarg = 'vendor_id'
    lookup_field = 'id'
    # permission_classes = [IsAuthenticated]