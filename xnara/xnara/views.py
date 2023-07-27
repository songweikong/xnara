from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from xnara.xnara.serializers import CustomerSerializer, PackInfoSerializer
from .models import Customer

# Create your views here.

# model viewset to get customer order based on customer_id
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


    @action(detail=True, methods=['get'])
    def get_customer_order(self, request, pk=None):
        # get customer object from database
        customer = Customer.objects.get(customer_id=pk)
        # if customer does not exist, return 400 error with message
        if customer is None:
            return Response("Customer id does not exist", status=400)
        # get customer order from two other apis
        json = customer.get_formatted_data()
        serializer = PackInfoSerializer(data=json)
        return Response(serializer.data)
