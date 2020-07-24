import paramiko


class SSH:
    """
    Базоывый класс для подключения по SSH и выполнения комманд
    """
    def __init__(self, **kwargs):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.kwargs = kwargs

    def exec_cmd(self, cmd, password=None):
        ''' Выполнить команду с помощью скрипта (к прим. ls -al)'''
        stdin, stdout, stderr = self.client.exec_command(cmd)

        # Если вызоы с правами админа
        if password:
            stdin.write('{password}\n')
            stdin.flush()

        data = stdout.read()
        if stderr:
            raise stderr
        return data.decode()

    def sudo_exec_cmd(self, cmd, password=''):
        ''' Выполнить команду с помощью скрипта (к прим. rm -rf) с правами sudo'''
        cmd = 'sudo' + cmd
        self.exec_cmd(cmd, password)

    def install_base_util(self):
        self.sudo_exec_cmd('apt-get update')
        self.sudo_exec_cmd('apt-get install \
                            apt-transport-https \
                            ca-certificates \
                            curl \
                            gnupg-agent \
                            software-properties-common')
        self.sudo_exec_cmd('apt install git')
        self.sudo_exec_cmd('apt install git')
        self.sudo_exec_cmd('curl -fsSL https://get.docker.com -o get-docker.sh')
        self.sudo_exec_cmd('sh get-docker.sh')


    def __enter__(self):
        kw = self.kwargs
        self.client.connect(hostname=kw.get('hostname'), username=kw.get('username'),
                            password=kw.get('password'), port=int(kw.get('port', 22)))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
