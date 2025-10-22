from typing import Optional, Iterable
from .models import User

def list_users() -> Iterable[User]:
    return User.objects.all()

def get_by_nick(nick: str) -> Optional[User]:
    return User.objects.filter(pk=nick).first()

def create_user(data: dict) -> User:
    return User.objects.create(**data)

def update_user(nick: str, data: dict) -> Optional[User]:
    obj = User.objects.filter(pk=nick).first()
    if not obj:
        return None
    for field, value in data.items():
        setattr(obj, field, value)
    obj.save()
    return obj

def delete_user(nick: str) -> bool:
    obj = User.objects.filter(pk=nick).first()
    if not obj:
        return False
    obj.delete()
    return True
