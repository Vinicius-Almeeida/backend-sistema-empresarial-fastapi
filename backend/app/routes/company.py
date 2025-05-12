from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models.company import Company
from app.schemas.company_schemas import CompanyCreate, CompanyResponse
from app.auth.auth_dependency import get_current_user
from app.models.user import User
from app.controllers.company_controller import (
    create_company,
    get_company_by_id,
    get_all_companies,
    delete_company,
    update_company
)

router = APIRouter(prefix="/companies", tags=["Empresas"])

@router.post("/", response_model=CompanyResponse)
def create(company_data: CompanyCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role.value != "admin":
        raise HTTPException(
            status_code=403,
            detail="Você não tem permissão para criar empresas"
        )
    return create_company(db, company_data)

@router.get("/{company_id}", response_model=CompanyResponse)
def read(company_id: int, db: Session = Depends(get_db)):
    company = get_company_by_id(db, company_id)
    if not company:
        raise HTTPException(
            status_code=404,
            detail="Empresa não encontrada"
        )
    return company

@router.get("/", response_model=list[CompanyResponse])
def read_all(db: Session = Depends(get_db)):
    return get_all_companies(db)

@router.put("/{company_id}", response_model=CompanyResponse)
def update(company_id: int, company_data: CompanyCreate, db: Session = Depends(get_db)):
    company = update_company(db, company_id, company_data.name)
    if not company:
        raise HTTPException(
            status_code=404,
            detail="Empresa não encontrada"
        )
    return company

@router.delete("/{company_id}")
def delete(company_id: int, db: Session = Depends(get_db)):
    deleted = delete_company(db, company_id)
    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Empresa não encontrada"
        )
    return {"detail": "Empresa deletada com sucesso"}