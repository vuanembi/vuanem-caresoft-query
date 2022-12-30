from typing import Optional

from pydantic import BaseModel


class CustomerResponse(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    date_of_birth: Optional[str]
    loyalty_points: Optional[str]
    loyalty_group: Optional[str]