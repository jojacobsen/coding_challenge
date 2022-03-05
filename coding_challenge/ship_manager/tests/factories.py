from typing import Any, Sequence

from coding_challenge.ship_manager.models import Ship
from factory.django import DjangoModelFactory
import datetime


class ShipFactory(DjangoModelFactory):
    code = "AAAA-1111-A1"
    created = datetime.datetime.now()
    updated = datetime.datetime.now()
    name = "USS Gerald R. Ford (CVN-78)"
    length = 337.1
    width = 78

    class Meta:
        model = Ship
        django_get_or_create = ["code"]
