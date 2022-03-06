from django.views.generic import ListView
from coding_challenge.ship_manager.models import Ship


class ShipListView(ListView):
    """
    Simple ListView to present all
    available lists on homepage.
    """

    model = Ship
    paginate_by = 100  # pagination
    ordering = "-created"  # newest ship first
