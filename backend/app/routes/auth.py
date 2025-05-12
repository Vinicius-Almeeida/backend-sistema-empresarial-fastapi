from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.database.session import SessionLocal
from app.models.user import User, UserRole
from app.models.company import Company
from app.auth.jwt_handler import create_access_token
from app.core.config import settings
from pydantic import BaseModel

router = APIRouter()

# Contexto para hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Schemas de entrada
class RegisterSchema(BaseModel):
    username: str
    password: str
    company_name: str
    role: UserRole

class LoginSchema(BaseModel):
    username: str
    password: str

# ROTA: Registro
@router.post("/register")
def register_user(user_data: RegisterSchema, db: Session = Depends(get_db)):
    # Verifica se usuário já existe
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    # Cria ou busca empresa
    company = db.query(Company).filter(Company.name == user_data.company_name).first()
    if not company:
        company = Company(name=user_data.company_name)
        db.add(company)
        db.commit()
        db.refresh(company)

    # Cria novo usuário
    hashed_password = pwd_context.hash(user_data.password)
    new_user = User(
        username=user_data.username,
        hashed_password=hashed_password,
        role=user_data.role,
        company_id=company.id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token(data={"sub": new_user.username, "role": new_user.role.value})
    return {"access_token": token, "token_type": "bearer"}

# ROTA: Login
@router.post("/login")
def login_user(login_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == login_data.username).first()
    if not user or not pwd_context.verify(login_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token(data={"sub": user.username, "role": user.role.value})
    return {"access_token": token, "token_type": "bearer"}

from app.auth.auth_dependency import get_current_user

@router.get("/me")
def get_logged_user(user: User = Depends(get_current_user)):
    return {
        "username": user.username,
        "role": user.role.value,
        "company": user.company.name
    }