from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class Ship(models.Model):
    """
    Ship model with following fields:

    created: Date Time Field with auto add at object created
    updated: Date Time Field with auto add at object update
    name: String with max length 255 characters
    length: Decimal Field for the length of the ship in meter (max. 5 digits and 2 decimal places)
    width: Decimal Field for the width of the ship in meter (max. 5 digits and 2 decimal places)
    code: Unique String for vessel identification that must follow this regex: [A-Z]{4}-[0-9]{4}-[A-Z][0-9]$
          e.g. AAAA-1111-A1
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(_("Name of Ship"), max_length=255)
    length = models.DecimalField(
        verbose_name=_("Length"),
        max_digits=5,
        decimal_places=2,
        help_text=_("Ship length in meter"),
    )
    width = models.DecimalField(
        verbose_name=_("Width"),
        max_digits=5,
        decimal_places=2,
        help_text=_("Ship width in meter"),
    )
    code = models.CharField(
        _("Unique Ship Code"),
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                r"[A-Z]{4}-[0-9]{4}-[A-Z][0-9]$",
                message=_(
                    "Code does not meet following regex [A-Z]{4}-[0-9]{4}-[A-Z][0-9]$"
                ),
            ),
        ],
    )

    def __str__(self):
        """
        Utilizes ship code as
        representation string.
        :return code:
        """
        return self.code

    class Meta:
        verbose_name = _("Ship")
        verbose_name_plural = _("Ships")
