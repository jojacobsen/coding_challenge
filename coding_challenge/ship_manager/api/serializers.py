from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework.validators import UniqueValidator

from coding_challenge.ship_manager.models import Ship


class ShipSerializer(serializers.ModelSerializer):
    """
    Model Serializer for
    Ship Model representation
    """

    # enforcing regex and unique validator
    # on code field

    code = serializers.RegexField(
        regex=r"[a-zA-Z]{4}-[0-9]{4}-[a-zA-Z][0-9]$",
        help_text=_("Please provide following code structure: AAAA-1111-A1"),
        error_messages={
            "invalid": _(
                "Code does not meet following regex [a-zA-Z]{4}-[0-9]{4}-[a-zA-Z][0-9]$"
            )
        },
        validators=[UniqueValidator(queryset=Ship.objects.all(), lookup="iexact")],
    )
    # Read Only for auto create fields
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Ship
        # following fields are enabled in the ship serializer
        fields = ["name", "length", "width", "code", "url", "created", "updated"]

        # add extra url field to create reverse path to ship object
        extra_kwargs = {"url": {"view_name": "api:ship-detail", "lookup_field": "code"}}

    def create(self, validated_data):
        # Make code string always upper case
        validated_data["code"] = validated_data["code"].upper()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Make code string always upper case if available
        if "code" in validated_data:
            validated_data["code"] = validated_data["code"].upper()
        return super().update(instance, validated_data)
