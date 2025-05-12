from pydantic import BaseModel, EmailStr
from typing import Optional

#Schema para criar um novo usuário
class UserCreate(BaseModel):
    username: EmailStr
    password: str
    role: str # 'admin' ou 'client'
    company_id: int

# Schema para exibir um usuário
class UserResponse(BaseModel):
    id: int
    username: EmailStr
    role: str
    company_id: int

    class config:
        from_attributes = True

# Schema para atualizar um usuário
class UserUpdate(BaseModel):
    username: EmailStr
    role: str
    company_id: int
    
    class Config:
        from_attributes = True
