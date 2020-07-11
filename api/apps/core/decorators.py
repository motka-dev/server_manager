from typing import ClassVar


def catching_base_exception() -> ClassVar:
    def wrapper(func):
        try:
            func()
        except Exception as exc:
            # TO DO
            # - logger
            print(exc)
    return wrapper