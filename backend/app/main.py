from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.session import engine, Base
from app.routes import auth
from app.routes import company
from app.routes import user
from fastapi.security import OAuth2PasswordBearer
from fastapi.openapi.utils import get_openapi
from fastapi import Depends

# Cria todas as tabelas automaticamente no banco com base nos modelos
Base.metadata.create_all(bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI(
    title="TRIXEL API - MVP 1",
    description="Sistema de automação com IA modular - TRIXEL",
    version="1.0.0"
)

# Permite que o frontend (React) acesse a API
origins = ["http://localhost:5173"]  # Porta padrão do Vite (React)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas de autenticação
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# Rota de teste da API
@app.get("/")
def read_root():
    return {"message": "TRIXEL API no ar"}

# Inclui as rotas de empresas
app.include_router(company.router, tags=["Empresas"])

# Inclui as rotas de usuários
app.include_router(user.router, tags=["Users"])

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Rotas
app.include_router(auth.router, tags=["Autenticação"])
app.include_router(company.router, tags=["Empresas"])
app.include_router(user.router, tags=["Usuários"])

# OpenAPI customizado para exibir o campo "Authorize" corretamente
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="TRIXEL API",
        version="1.0.0",
        description="Documentação da API TRIXEL",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", []).append({"BearerAuth": []})
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
