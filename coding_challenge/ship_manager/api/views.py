from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from coding_challenge.ship_manager.models import Ship
from coding_challenge.ship_manager.api.serializers import ShipSerializer


class ShipViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet for viewing and editing ships.
    CRUD functionality is enabled for the Ship model.
    User Authentication is required.
    """
    queryset = Ship.objects.all()
    serializer_class = ShipSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "code"
