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
        return f"{self.server_name} {self.is_connected}"

    def __str__(self):
        return f"{self.server_name} {self.is_connected}"

    class Meta:
        db_table = 'servers'
        ordering = ['-created']
        verbose_name = verbose_name_plural = "Servers"



class ConnectorType(models.Model):
    """
    Server connector type
    example: SSH, FTP, ...
    """
    name = models.CharField(verbose_name="Connection type name", max_length=64)

    class Meta:
        db_table = 'connector_types'
        verbose_name = verbose_name_plural = "Server connector types"

class SimpleSSHConnector(models.Model):
    """
    Describes the ssh server's connection
    """
    server_ip = models.GenericIPAddressField(
        verbose_name='Server ip to connections'
    )

    ssh_username = models.CharField(
        verbose_name='SSH. Username for connection to server',
        max_length=64,
        null=False,
    )

    server_ref = models.OneToOneField(
        verbose_name='SSH. Password for connection to server',
        to=Server,
        on_delete=models.CASCADE,
        default=None,
    )

    connector_type_ref = models.OneToOneField(
        verbose_name="Connection type ref",
        to=ConnectorType,
        null=False,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f"{self.ssh_username}"

    class Meta:
        db_table = 'simple_ssh_connections'
        verbose_name = verbose_name_plural = "Simple SSH connectors"
