from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.controllers.user_controller import create_user, get_all_users, get_users_by_company, update_user, delete_user
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.auth.auth_dependency import get_current_user
from app.models.user import User


router = APIRouter(prefix="/users", tags=["Usuários"])

# Cria um novo usuário
@router.post("/", response_model=UserResponse)
def create(
    user: UserCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
    ):

    if current_user.role.value != "admin":
        raise HTTPException(
        status_code=403,
        detail="Você não tem permissão para criar usuários")
    
    return create_user(db, user)

# Retorna todos os usuários
@router.get("/", response_model=list[UserResponse])
def read_all(
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
    ):

    if current_user.role != "admin":
        return get_all_users(db)
    
    return get_users_by_company(db, current_user.company_id)

# Atualiza um usuário
@router.put("/{user_id}", response_model=UserResponse)
def update_user_route(
    user_id: int, 
    user: UserUpdate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    if current_user.role.value != "admin":
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para atualizar usuários")

    return update_user(db, user_id, user)


# Deleta um usuário
@router.delete("/{user_id}", status_code=200)
def delete_user(
    user_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
    ):

    if current_user.role.value != "admin":
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para deletar usuários")
    
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado")
    
    db.delete(user) 
    db.commit()
    return {"message": "Usuário deletado com sucesso"}
    
