from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.hashers import make_password
from django.contrib.postgres.fields import JSONField

from polymorphic.models import PolymorphicModel

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

    def __str__(self) -> str:
        return f"{self.server_name} {self.is_connected}"

    class Meta:
        db_table = 'server_config'
        ordering = ['-created']
        verbose_name = verbose_name_plural = "Servers config"


class BaseConnector(PolymorphicModel):
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
        to=ServerConfig,
        on_delete=models.CASCADE,
        related_name='connector'
    )

    class Meta:
        pass
        #abstract = True


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
        return f"username: {self.ssh_username}, \
        ip: {self.connection_ip}, \
        port: {self.connection_port}"

    class Meta:
        db_table = 'simple_ssh_connections'
        verbose_name = verbose_name_plural = "Simple SSH connectors"


class KeySSHConnector(BaseConnector):
    """
    Describes the ssh server's connection
    by RSA key's
    """
    ssh_pubkey = models.TextField(
        verbose_name='SSH. Public RSA key connection to server',
        null=False,
    )

    def str(self) -> str:
        return self.ssh_pubkey

    class Meta:
        db_table = 'key_ssh_connections'
        verbose_name = verbose_name_plural = "RSA key SSH connectors"
