import pytest
from django.urls import reverse

from coding_challenge.ship_manager.models import Ship

pytestmark = pytest.mark.django_db


class TestShipAdmin:
    """
    Test Admin view for Ship Model.
    """
    def test_changelist_ship_admin(self, admin_client):
        url = reverse("admin:ship_manager_ship_changelist")
        response = admin_client.get(url)
        assert response.status_code == 200

    def test_ship_admin_search(self, admin_client):
        url = reverse("admin:ship_manager_ship_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == 200

    def test_view_ship_admin(self, admin_client):
        ship = Ship.objects.create(name="Queen Mary", code="ABCD-1111-A9", width=12.2, length=36.6)
        url = reverse("admin:ship_manager_ship_change", kwargs={"object_id": ship.pk})
        response = admin_client.get(url)
        assert response.status_code == 200
