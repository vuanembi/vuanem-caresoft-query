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
