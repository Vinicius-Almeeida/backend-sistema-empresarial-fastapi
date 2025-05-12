from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para criar um novo usuário
def create_user(db: Session, user_data: UserCreate):
    hashed_password = pwd_context.hash(user_data.password)
    new_user = User(
        username=user_data.username,
        hashed_password=hashed_password,
        role=user_data.role,
        company_id=user_data.company_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Função para obter todos os usuários
def get_all_users(db: Session):
    return db.query(User).all()

# Função para obter um usuário pelo ID
def get_users_by_company(db: Session, company_id: int):
    return db.query(User).filter(User.company_id == company_id).all()

# Função para atualizar um usuárioe
def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404, 
            detail="Usuário não encontrado")
    
    user.username = user_data.username
    user.role = user_data.role
    user.company_id = user_data.company_id
    db.commit()
    db.refresh(user)
    return user

# Função para deletar um usuário
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=404, 
            detail="Usuário não encontrado")    
    db.delete(user)
    db.commit()
    return {"message": "Usuário deletado com sucesso"} 

