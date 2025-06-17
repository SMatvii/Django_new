import pytest
from products.models import Category, Product, Order
from .fixtures import category, product, product_with_discount, order, OrderItem


@pytest.fixture
def category():
    return Category.objects.create(name="test_category_fixtures")


@pytest.fixture
def product():
    category =Category.objects.create(
        name = 'test-category'
    )
    product = Product.objects.create(
        name = 'test-product',
        category=category.id,
        nomenclature = 'test-nomenclature',
        price = 100
    )
    return product

@pytest.fixture
def product_with_discount():
    category = Category.objects.create(name="test_user")
    return Product.objects.create(
        name="test_product",
        category=category.id,
        nomenclature="test_nomenclature",
        price=100,
        discount=20  
    )
    
@pytest.fixture
def order(user, product, product_with_discount):
    order = Order.objects.create(
        user=user,
        contact_name="test_contact",
        contact_phone="380322312",
        contact_email="testemail1@gmail.com",
        address="test_address",
    )
    
    OrderItem.objects.create(
        order=order,
        product=product,
        price=100
    )
    
    OrderItem.objects.create(
        order=order,
        product=product_with_discount,
        amount=2,
        price=80
    ) 
    
    return order
