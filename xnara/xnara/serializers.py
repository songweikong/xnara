# serializers.py
from rest_framework import serializers
from .models import Customer

# serializer for customer id
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id',)

# serializer to get customer packs
class PackInfoSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    pack1 = serializers.JSONField()
    pack2 = serializers.JSONField()
    id = serializers.IntegerField()
