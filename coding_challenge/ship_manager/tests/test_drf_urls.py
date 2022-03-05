import pytest
from django.urls import resolve, reverse

from coding_challenge.ship_manager.models import Ship

pytestmark = pytest.mark.django_db


def test_ship_list():
    """
    Test ship list urls.
    """
    assert reverse("api:ship-list") == "/api/ships/"
    assert resolve("/api/ships/").view_name == "api:ship-list"


def test_ship_detail(ship: Ship):
    """
    Test ship detail urls.
    """
    assert (
        reverse("api:ship-detail", kwargs={"code": ship.code})
        == f"/api/ships/{ship.code}/"
    )
    assert resolve(f"/api/ships/{ship.code}/").view_name == "api:ship-detail"
