import pytest

from django.urls import reverse

from .fixtures import product, product_with_discount


@pytest.mark.django_db
def test_product_list_empty(api_client):
    url = reverse("products:product-list")
    
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert response.data ==  []


@pytest.mark.django_db
def test_product_list_endpoint(api_client, product, product_with_discount):
    url = reverse("products:product-list")
    
    response = api_client.get(url)
    
    assert response.status_code == 200
    assert len ==  []