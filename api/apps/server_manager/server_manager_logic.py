from .kits.ssh_base import SSH
from api.apps.core.decorators import catching_base_exception


@catching_base_exception
def init_server(ip: str, port: int, user_name: str, password: str) -> None:
    with SSH(hostname=ip, username=user_name, password=password, port=port) as ssh:
        out = ssh.exec_cmd('ls -l')
        print(out)