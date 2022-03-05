import pytest

from coding_challenge.users.models import User
from coding_challenge.users.tests.factories import UserFactory
from coding_challenge.ship_manager.models import Ship
from coding_challenge.ship_manager.tests.factories import ShipFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    return UserFactory()


@pytest.fixture
def ship() -> Ship:
    return ShipFactory()
