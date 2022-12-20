from sqlalchemy.sql import func

from app.database.base import Session
from app.zalo.user_model import ZaloUser


def add_user(user_id, phone):
    with Session() as session:
        user = ZaloUser(user_id=user_id, phone=phone)
        session.add(user)
        session.commit()


def update_user(id, user_id, phone):
    with Session() as session:
        user = {"user_id": user_id, "phone": phone}
        session.query(ZaloUser).filter(ZaloUser.id == id).update(user)
        session.commit()


def delete_user(user_id):
    with Session() as session:
        session.query(ZaloUser).filter(ZaloUser.user_id == user_id).update(
            {"deleted_date": func.now()}
        )
        session.commit()
