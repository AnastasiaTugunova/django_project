from rest_framework import serializers
from logistic.models import Product, Stock, StockProduct
from rest_framework.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        def validate_text(self, value):
            if 'product' in value:
                raise ValidationError('Неверное название продукта')
            return value

class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        for position in positions:
            stock_create = StockProduct.objects.create(stock=stock, **position)
            stock_create.save()
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        for position in positions:
            up_stock_product = StockProduct.objects.update_or_create(
                stock=stock,
                product=position['product'],
                defaults={
                    'stock': stock,
                    'product': position['product'],
                    'quantity': position['quantity'],
                    'price': position['price']
                }
            )
            up_stock_product.save()
        return stock
