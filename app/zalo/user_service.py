from sqlalchemy.sql import func

from app.database.base import Session
from app.zalo.user_model import ZaloUser

from app.zalo.user_schema import UserCreate


def add_user(user: UserCreate):
    with Session() as session:
        user = ZaloUser(user_id=user.user_id, phone=user.phone)
        session.add(user)
        session.commit()


def update_user(id, user: UserCreate):
    with Session() as session:
        user = {"user_id": user.user_id, "phone": user.phone}
        session.query(ZaloUser).filter(ZaloUser.id == id).update(user)
        session.commit()


def delete_user(user_id):
    with Session() as session:
        session.query(ZaloUser).filter(ZaloUser.user_id == user_id).update(
            {"deleted_date": func.now()}
        )
        session.commit()


def get_user(user: UserCreate):
    with Session() as session:
        user = {"user_id": user.user_id, "phone": user.phone}
        users = session.query(ZaloUser).filter_by(**user)
        return users
