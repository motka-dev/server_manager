from typing import Dict


def get_default_server_settings() -> Dict:
    DEFAULT_SERVER_SETTINGS: dict = {
            'POSTFIX': {
                'ip': '127.0.0.1',
                'port': '52'
            },
            'BIND': {
                'kek': 'lol'
            }
    }
    return DEFAULT_SERVER_SETTINGS
