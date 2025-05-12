from pydantic import BaseModel
from typing import Optional

# Schema para criação
class CompanyCreate(BaseModel):
    name: str

# Schema para Aresposta
class CompanyResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True