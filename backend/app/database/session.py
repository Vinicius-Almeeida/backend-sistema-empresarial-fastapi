from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Conexão com o banco usando URL do .env
engine = create_engine(settings.DATABASE_URL)

# Cria a fábrica de sessões para interações com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base usada nos models (User, Company, etc)
Base = declarative_base()

# Função para obter uma sessão no banco
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()