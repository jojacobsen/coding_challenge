import pytest

from coding_challenge.ship_manager.models import Ship

pytestmark = pytest.mark.django_db


def test_ship_object_representation(ship: Ship):
    """
    Test if ship object has correct representation string.
    """
    assert ship.__str__() == ship.code


def test_ship_object_creation(ship: Ship):
    """
    Test if ship object is able to get created and updated in db.
    """
    s = Ship(name="Queen Mary", code="ABCD-1111-A9", width=12.2, length=36.6)
    s.save()
    ship_instance = Ship.objects.get(code='ABCD-1111-A9')
    initial_update_time = ship_instance.updated
    initial_creation_time = ship_instance.created
    assert ship_instance.name == 'Queen Mary'

    ship_instance.name = 'Queen Mary 2'
    ship_instance.save()
    # Check if update time changes and creation time
    # stays the same on object update
    assert initial_update_time != ship_instance.updated
    assert initial_creation_time == ship_instance.created
