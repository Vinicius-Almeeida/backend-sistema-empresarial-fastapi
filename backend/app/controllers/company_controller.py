from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company_schemas import CompanyCreate

def create_company(db: Session, company_data: CompanyCreate):
    new_company = Company(name=company_data.name)
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company

def get_company_by_id(db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()

def get_all_companies(db: Session):
    return db.query(Company).all()

def update_company(db: Session, company_id: int, name: str):
    company = db.query(Company).filter(Company.id == company_id).first()
    if company:
        company.name = name
        db.commit()
        db.refresh(company)
    return company

def delete_company(db: Session, company_id: int):
    company = db.query(Company).filter(Company.id == company_id).first()
    if company:
        db.delete(company)
        db.commit()
    return company