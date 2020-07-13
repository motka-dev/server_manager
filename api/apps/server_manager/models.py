from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib.postgres.fields import JSONField


from api.apps.core.models import CreationModificationDateBase
from api.apps.core.stage import get_default_server_settings

from .validators import validate_json_settings


class Server(CreationModificationDateBase):
    """
    Describes the user's server that will be monitored and configured
    """

    server_ip = models.GenericIPAddressField(
        verbose_name='Server ip to connections'
    )

    server_name = models.CharField(
        verbose_name='Server name to show in client',
        max_length=16,
        blank=False,
        null=False,
        default=get_random_string(length=8),
    )

    is_connected = models.BooleanField(
        verbose_name='Flag to show active servers',
        default=False,
    )

    server_settings = JSONField(
        verbose_name='JSON with settings for \
            SMTP(POSTFIX) and DNS(BIND) services',
        default=get_default_server_settings,
        validators=[validate_json_settings],
    )

    def __repr__(self):
        return f"{self.server_ip} {self.server_name}"

    def __str__(self):
        return f"{self.server_ip} {self.server_name}"

    class Meta:
        db_table = 'servers'
        ordering = ['-created']
        verbose_name = verbose_name_plural = "Servers"


class ServerConnection(models.Model):
    """
    Describes the ssh server's connection
    """
    ssh_username = models.CharField(
        verbose_name='SSH. Username for connection to server',
        max_length=64,
        null=False,
    )

    ssh_password = models.CharField(
        verbose_name='SSH. Password for connection to server',
        max_length=256,
        null=False,
    )

    server_ref = models.OneToOneField(
        verbose_name='SSH. Password for connection to server',
        to=Server,
        on_delete=models.CASCADE,
        default=None,
    )

    def save(self, **kwargs):
        """
        Create hash password field
        """
        self.ssh_password = make_password(self.ssh_password)
        super().save(**kwargs)

    def __str__(self):
        return f"{self.ssh_username}"

    class Meta:
        db_table = 'server_connections'
        verbose_name = verbose_name_plural = "Server connections"
