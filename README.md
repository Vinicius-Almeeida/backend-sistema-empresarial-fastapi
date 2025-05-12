
# 🧠  Sistema Empresarial com FastAPI

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/fastapi-%F0%9F%90%8D-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23blue.svg)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)

> Um sistema inteligente de gestão empresarial, modular, seguro e escalável. Idealizado para empresas que buscam performance, automação e facilidade de uso.

---

## 🔥 Visão Geral

O **TRIXEL** é um sistema backend robusto construído com **FastAPI**, que traz uma base sólida para controle de usuários, autenticação JWT, múltiplas filiais e modularidade total.  

Pensado para escalar, com separação clara entre rotas, controllers, modelos e schemas, além de autenticação avançada para APIs protegidas.

---

## 🧩 Tecnologias Utilizadas

| Backend | Banco de Dados | Segurança | Outros |
|--------|----------------|-----------|--------|
| 🐍 Python 3.11 | 🐘 PostgreSQL | 🔐 JWT Auth | ⚙️ Pydantic |
| 🚀 FastAPI | 📦 SQLAlchemy | 🔧 OAuth2 Password Flow | 🧪 Uvicorn |

---

## 📁 Estrutura do Projeto

```
trixel/
│
├── backend/
│   ├── app/
│   │   ├── auth/
│   │   ├── controllers/
│   │   ├── core/
│   │   ├── database/
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │   └── main.py
│   ├── requirements.txt
│   └── venv/ (ignorado)
│
├── .gitignore
└── README.md
```

---

## ✅ Funcionalidades

- [x] CRUD de usuários e empresas
- [x] Login com autenticação JWT
- [x] Modularização por domínio
- [x] Proteção de rotas com OAuth2
- [x] Banco relacional PostgreSQL
- [ ] Dashboard de análise
- [ ] Integração com frontend (React)

---

## ⚙️ Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/Vinicius-Almeeida/backend-sistema-empresarial-fastapi.git
cd backend-sistema-empresarial-fastapi/backend

# Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor local
uvicorn app.main:app --reload
```

---

## 🔐 Autenticação JWT

- Token gerado via login (`/auth/login`)
- Necessário para acessar rotas protegidas com `Depends(oauth2_scheme)`
- Os usuários têm dados persistidos em banco e são verificados por senha + token.

---

## 🎯 Próximos passos

- [ ] Adicionar painel administrativo
- [ ] Criar relatórios PDF com exportações
- [ ] Deploy com Docker + CI/CD
- [ ] Integração com frontend (React TRIXEL UI)

---

## 🧠 Diagrama Lógico (simplificado)

```
Usuário → Login → JWT Token ↴
       └──→ Rotas protegidas (GET/POST) → Controller → Model → DB
```

---

## 🧑‍💻 Autor

**Vinícius Almeida**  
[LinkedIn](https://www.linkedin.com/in/vinicius-quadros1990/)  
Desenvolvedor Full Stack em transição de carreira e apaixonado por criar soluções reais com impacto direto em negócios.

---

## 🫡 Licença

Este projeto está sob a licença MIT. Sinta-se livre para utilizar, estudar, modificar e melhorar!

---

## 💬 Feedback

Curtiu o projeto? Tem ideias ou sugestões? Me chama no LinkedIn ou abre uma issue no repositório!

---
