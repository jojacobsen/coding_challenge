import pytest
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from coding_challenge.users.models import User

from coding_challenge.ship_manager.models import Ship

pytestmark = pytest.mark.django_db


def test_ship_view_auth(user: User, ship: Ship):
    """
    Ensure that the endpoints are only accessible for authenticated user.
    """

    client = APIClient()
    url = reverse("api:ship-list")
    data: dict = {}
    response = client.post(url, data, format='json')
    # Test unauthorized API call (get, post, delete, put)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    response = client.get(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    url = reverse("api:ship-detail", kwargs={"code": ship.code})
    response = client.delete(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN
    url = reverse("api:ship-detail", kwargs={"code": ship.code})
    response = client.put(url)
    assert response.status_code == status.HTTP_403_FORBIDDEN


def test_list_ship(user: User, ship: Ship):
    """
    Ensure we can get the list of ship objects.
    """

    client = APIClient()
    token, created = Token.objects.get_or_create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    url = reverse("api:ship-list")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)


def test_detail_ship_view(user: User, ship: Ship):
    """
    Ensure we can get a single of ship object.
    """

    client = APIClient()
    token, created = Token.objects.get_or_create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    url = reverse("api:ship-detail", kwargs={"code": ship.code})
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)


def test_create_ship(user: User, ship: Ship):
    """
    Ensure we can create a new ship object.
    """

    client = APIClient()
    url = reverse("api:ship-list")
    data: dict = {}
    token, created = Token.objects.get_or_create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    # Call API with invalid data
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Test ship creating with invalid code
    data = {
        'code': 'test-ship',
        'name': 'test-ship',
        'width': 31,
        'length': 10,
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'code' in response.data

    # Test ship creating with no unique code
    data['code'] = 'AAAA-1111-A1'
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'code' in response.data

    # Test ship creating with valid data
    data['code'] = 'AAAA-1111-A9'
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Ship.objects.count() == 2


def test_update_ship(user: User, ship: Ship):
    """
    Ensure we can update a ship object.
    """

    client = APIClient()
    token, created = Token.objects.get_or_create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    url = reverse("api:ship-detail", kwargs={"code": ship.code})
    response = client.patch(url, data={'name': 'Aida'})
    assert response.status_code == status.HTTP_200_OK
    ship_instance = Ship.objects.get(code=ship.code)
    assert ship_instance.name == 'Aida'


def test_delete_ship(user: User, ship: Ship):
    """
    Ensure we can delete a ship object.
    """

    client = APIClient()
    token, created = Token.objects.get_or_create(user=user)
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    url = reverse("api:ship-detail", kwargs={"code": ship.code})
    response = client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Ship.objects.count() == 0
