from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ShipManagerConfig(AppConfig):
    """
    Register Ship Manager app in project.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "coding_challenge.ship_manager"
    verbose_name = _("Ship Manager")
