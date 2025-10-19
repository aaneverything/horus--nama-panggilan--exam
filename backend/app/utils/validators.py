import re
from email.utils import parseaddr


def validate_email(email: str) -> bool:
    if not email:
        return False
    _, addr = parseaddr(email)
    return bool(re.match(r"^[^@]+@[^@]+\.[^@]+$", addr))


def validate_password(pw: str) -> bool:
    return bool(pw and len(pw) >= 8 and re.search(r"[A-Za-z]", pw) and re.search(r"\d", pw))