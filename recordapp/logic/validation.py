# logic/validation.py
from datetime import datetime


def validate_date(date_str: str) -> bool:
    """Valida formato YYYY-MM-DD"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except Exception:
        return False


def validate_description(desc: str) -> bool:
    """Descripción no vacía y no solo espacios"""
    if desc and desc.strip():
        return True
    return False
