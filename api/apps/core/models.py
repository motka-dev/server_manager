from django.db import models
from django.utils.translation import gettext_lazy as _


class CreationModificationDateBase(models.Model):
    """
    Abstract base class with creation and modification date
    """
    created = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )

    modificated = models.DateTimeField(
        _("Modificated at"),
        auto_now=True,
    )

    class Meta:
        abstract = True
