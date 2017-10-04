from rest_framework import serializers

from . import models

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'description',
            'url',
        )
        model = models.ProductType

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'title',
            'url',
        )
        model = models.Category

class ProductSerializer(serializers.ModelSerializer):

    productType = ProductTypeSerializer(read_only=True)
    category = CategorySerializer(read_only=True);

    class Meta:
        fields = (
            'create_at',
            'unit_price',
            'count',
            'unit_type',
            'available_at',
            'productType',
            'category'
        )
        model = models.Product

class ProductOrderSerializer(serializers.ModelSerializer):

    productType = ProductTypeSerializer(read_only=True)
    category = CategorySerializer(read_only=True);

    class Meta:
        fields = (
            'unit_type',
            'productType',
            'category'
        )
        model = models.Product

class PaymentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'title'
        )
        model = models.PaymentType

class PaymentSerializer(serializers.ModelSerializer):

    paymentType = PaymentTypeSerializer(read_only=True)

    class Meta:
        fields = (
            'amount',
            'state',
            'paymentType'
        )
        model = models.Payment

class OrderItemSerializer(serializers.ModelSerializer):

    product = ProductOrderSerializer(read_only=True)

    class Meta:
        fields = (
            'count',
            'product'
        )
        model = models.Order_Item

class OrderSerializer(serializers.ModelSerializer):

    order_item = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        fields = (
            'delivery_at',
            'shipping_address',
            'order_item',
        )
        model = models.Order