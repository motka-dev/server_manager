from django.db import models
from django.utils.crypto import get_random_string
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from api.apps.core.models import CreationModificationDateBase


class Server(CreationModificationDateBase):
    """
    Describes the user's server that will be monitored and configured
    """
    class ServerStatus(models.TextChoices):
        """
        Describes the server state
        """
        WORKING = 'WR', _('WORKING')
        PAUSED = 'PS', _('PAUSED')
        STOPPED = 'ST', _('STOPPED')

    server_ip = models.GenericIPAddressField()

    server_name = models.CharField(max_length=16,
                                   blank=False,
                                   null=False,
                                   default=get_random_string(length=8))

    is_connected = models.BooleanField(default=False)

    status = models.CharField(choices=ServerStatus.choices,
                              default=ServerStatus.STOPPED,
                              max_length=2)

    def __repr__(self):
        return f"{self.server_ip} {self.server_name}"

    def __str__(self):
        return f"{self.server_ip} {self.server_name}"
    # TO DO:
    # - server config: JSON
    #

    class Meta:
        db_table = 'server'
        ordering = ['-created']
        verbose_name = verbose_name_plural = "Servers"


class ServerConnection(models.Model):
    """
    Describes the ssh server's connection
    """
    ssh_username = models.CharField(max_length=64,
                                    null=False)

    ssh_password = models.CharField(max_length=256,
                                    null=False)

    server = models.OneToOneField(to=Server,
                                  on_delete=models.CASCADE)

    def save(self, **kwargs):
        """
        Create hash password field
        """
        self.ssh_password = make_password(self.ssh_password)
        super().save(**kwargs)

    def __str__(self):
        return f"{self.ssh_username}"

    class Meta:
        db_table = 'server_connection'
        verbose_name = verbose_name_plural = "Server connections"
