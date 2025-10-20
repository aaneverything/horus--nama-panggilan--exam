from sqlalchemy import select
from ..extensions import db
from typing import Any, Mapping, Tuple
from ..models.user import User
from flask import abort
from ..utils.validators import validate_email, validate_password


def create_user(data: Mapping[str, Any]) -> Tuple[User | None, str | None]:
    username = (data.get("username") or "").strip()
    email = (data.get("email") or "").strip().lower()
    nama = (data.get("nama") or "").strip()
    password = data.get("password") or ""

    if not username or not nama:
        return None, "missing_fields"
    if not validate_email(email):
        return None, "invalid_email"
    if not validate_password(password):
        return None, "weak_password"

    if db.session.scalar(select(User).filter_by(username=username)):
        return None, "username_taken"
    if db.session.scalar(select(User).filter_by(email=email)):
        return None, "email_taken"

    u = User()
    u.username = username
    u.email = email
    u.nama = nama
    u.set_password(password)
    db.session.add(u)
    db.session.commit()
    return u, None


def get_user(user_id: int) -> User:
    u = db.session.get(User, user_id)
    if not u:
        abort(404, description="User tidak ditemukan")
    return u


def authenticate_user(username: str | None, password: str | None):
    if not username or not password:
        return None
    user = db.session.scalar(select(User).filter_by(username=username.strip()))
    if user and user.check_password(password):
        return user
    return None


def list_users():
    return db.session.scalars(select(User).order_by(User.id.asc())).all()


def update_user(user_id: int, data: Mapping[str, Any]):
    u = db.session.get(User, user_id)
    if not u:
        return None, "Not_found"

    new_username = data.get("username")
    new_email = data.get("email")
    new_nama = data.get("nama")

    from sqlalchemy import and_

    if new_username:
        new_username = new_username.strip()
        exists = db.session.scalar(
            select(User).where(and_(User.username == new_username, User.id != user_id))
        )
        if exists:
            return None, "username_taken"
        u.username = new_username

    if new_email:
        new_email = new_email.strip().lower()
        exists = db.session.scalar(
            select(User).where(and_(User.email == new_email, User.id != user_id))
        )
        if exists:
            return None, "email_taken"
        u.email = new_email

    if new_nama:
        u.nama = new_nama.strip()

    db.session.commit()
    return u, None


def delete_user(user_id: int):
    u = db.session.get(User, user_id)
    if not u:
        return False, "not_found"
    db.session.delete(u)
    db.session.commit()
    return True, None
