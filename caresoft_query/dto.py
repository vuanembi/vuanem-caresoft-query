from typing import Optional

from pydantic import BaseModel


class CustomerResponse(BaseModel):
    date_of_birth: Optional[str]
    email: Optional[str]
    id: Optional[str]
    loyalty_group: Optional[str]
    loyalty_points: Optional[str]
    name: Optional[str]
    phone: Optional[str]


class OrderBase(BaseModel):
    id: Optional[int]
    tranid: Optional[str]


class Item(BaseModel):
    sku: Optional[str]
    quantity: Optional[int]
    amount: Optional[float]


class Order(BaseModel):
    id: Optional[int]
    tranid: Optional[str]
    trandate: Optional[str]
    items: list[Item]
