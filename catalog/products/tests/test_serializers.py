import pytest


from products.serializers.order_serializers import  OrderSerializer
from products.serializers.product_serializers import ProductSerializer
from .fixtures import category, product_with_discount, product, order

@pytest.mark.django_db
def test_product_serializer_valid(category):
    data = {
        "name": "test_name",
        "description": "test_description",
        "stock":3,
        "price":100,
        "available": True,
        "category": category,
        "nomenclature":"test_nomenclature",
        "rating":2,
        "discount":10,
        "attributes": {}
    }
    
    serializer = ProductSerializer(data=data)
    
    assert serializer.is_valid()
    
@pytest.mark.django_db
def test_product_serializer_invalid(category):
    data = {
        "name": "*"*101,
        "description": {},
        "stock": -3,
        "price":-100,
        "available": 2,
        "nomenclature":"*"*101,
        "rating":"*",
        "discount":-10,
        "attributes": "*"
    }
    
    

    serializer = ProductSerializer(data=data)
    
    
    assert not serializer.is_valid()
    assert serializer.errors
    assert 'Ensure this field has no more than 100 characters.' in serializer.errors["name"]
    assert 'Must be a valid boolean.' in serializer.errors["available"]
    assert 'Ensure this field has no more than 50 characters.' in serializer.errors["nomenclature"]
    assert 'A valid number is required.' in serializer.errors["rating"]
    for field in data.keys():
        assert field in serializer.errors
    

@pytest.mark.django_db
def test_product_serializer_valid(category_fixtures):
    data = {
        "name": "test_name",
        "description": "test_description",
        "stock":3,
        "price":100,
        "available": True,
        "category": category_fixtures,
        "nomenclature":"test_nomenclature",
        "rating":2,
        "discount":10,
        "attributes": {}
    }
    
    serilaizer = ProductSerializer(data=data)
    
    assert serilaizer.is_valid()
    assert "category" not in serilaizer.data
    
@pytest.mark.django_db
def test_product_serializer_method_field(product_discount):
    serializer = ProductSerializer(product_discount)
    
    assert serializer.data['discount_price'] == product_discount.discount_price
    assert serializer.data['discount_price'] == 80
        
        
@pytest.mark.django_db
def test_order_serializer_readonly(user):
    data = {
        "user": user.id,
        "contcact_name": "test-name",
        "contact_email": "test@gmail.com",
        "contact_phone": "38093923232",
        "address": "test-address", 
    }
    
    serializer = OrderSerializer(data=data)
    
    assert serializer.is_valid()
    assert "items" not in serializer.validated_data
    
    order = serializer.save()
    
    serializer = OrderSerializer(order)
    
    assert "items" in serializer.data
        
        
@pytest.mark.django_db
def test_order_serializer_items(order):


    serializer = OrderSerializer(order)
    
    items = serializer.data["items"]
    
    assert len(items) == 2
    