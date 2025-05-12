from sqlalchemy import Column, Integer, String
from app.database.session import Base
from sqlalchemy.orm import relationship

# Modelo de empresa
class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    users = relationship("User", back_populates="company")