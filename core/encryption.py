from cryptography.fernet import Fernet

from config.settings import settings


cipher = Fernet(
    settings.ENCRYPTION_KEY.encode()
)


def encrypt(value: str) -> str:

    return cipher.encrypt(
        value.encode()
    ).decode()


def decrypt(value: str) -> str:

    return cipher.decrypt(
        value.encode()
    ).decode()