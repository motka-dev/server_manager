from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib.postgres.fields import JSONField

from api.apps.core.models import CreationModificationDateBase
from api.apps.core.stage import get_default_server_settings

from .validators import validate_json_settings


class ServerConfig(CreationModificationDateBase):
    """
    Describes the user's server that will be monitored and configured
    """
    server_name = models.CharField(
        verbose_name='Server name to show in client',
        max_length=16,
        blank=False,
        null=False,
        default=get_random_string(length=5),
    )

    server_settings = JSONField(
        verbose_name='JSON with settings for \
            SMTP(POSTFIX) and DNS(BIND) services',
        default=get_default_server_settings,
        validators=[validate_json_settings],
    )

    def __str__(self) -> str:
        return f"{self.server_name} {self.created}"

    class Meta:
        db_table = 'server_config'
        ordering = ['-created']
        verbose_name = verbose_name_plural = "Server's config's"


class BaseConnector(models.Model):
    """
    Describes the specific base connection model model

    """
    connection_ip = models.GenericIPAddressField(
        verbose_name='Server ip to connections'
    )

    connection_port = models.IntegerField(
        verbose_name='Server connection port',
        default=22
    )

    server_config = models.OneToOneField(
        verbose_name='Ref to server config',
        related_name='connector',
        to=ServerConfig,
        on_delete=models.CASCADE
    )

    is_connected = models.BooleanField(
        verbose_name='Flag to show active servers',
        default=False,
    )

    class Meta:
        db_table = 'base_connector'
        verbose_name = verbose_name_plural = "Base connectors's"

class SimpleSSHConnector(BaseConnector):
    """
    Describes the ssh server's connection
    by login and password
    """
    ssh_username = models.CharField(
        verbose_name='SSH. Username for connection to server',
        max_length=64,
        null=False,
    )
    def __str__(self) -> str:
        return f"{self.ssh_username}"

    class Meta:
        db_table = 'simple_ssh_connection'
        verbose_name = verbose_name_plural = "Simple SSH connector's"

