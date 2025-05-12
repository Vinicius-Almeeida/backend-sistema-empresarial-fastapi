from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database.session import Base
import enum

class UserRole(enum.Enum):
    admin = "admin"
    client = "client"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company")
