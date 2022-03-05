from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from coding_challenge.ship_manager.models import Ship


@admin.register(Ship)
class ShipAdmin(admin.ModelAdmin):
    """
    Register the Ship model within the admin interface,
    for easy maintenance and manual object creation.
    """
    list_display = ["code", "name", "length", "width"]
    search_fields = ["name", "code"]
    list_filter = ["length", "width"]
