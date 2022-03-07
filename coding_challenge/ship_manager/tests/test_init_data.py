import pytest
from django.core.management import call_command

from coding_challenge.ship_manager.models import Ship

pytestmark = pytest.mark.django_db


def test_load_ship_data_fixture():
    # Test loading fixtures
    call_command("loaddata", "ships", verbosity=0)

    assert Ship.objects.count() == 11
    ship = Ship.objects.get(pk="QMAB-3111-B2")
    assert ship.name == "Queen Merry"
