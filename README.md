# 🧪 Mi Primera API - By Freddy

_Un humilde experimento que... ¡sorprendentemente funciona!_

![FastAPI banner](./docs/banner.png)

---

## 🚀 Descripción

Esta es una API RESTful construida con **FastAPI** para gestionar clientes, planes de suscripción y transacciones.  
El objetivo principal fue aprender y practicar los fundamentos de desarrollo backend moderno usando Python, SQLModel y FastAPI.

---

## 🔧 Tecnologías Utilizadas

- **FastAPI** – Framework rápido para APIs con documentación automática.
- **SQLModel** – ORM moderno basado en Pydantic + SQLAlchemy.
- **SQLite / MySQL (opcional)** – Base de datos local o remota (Aurora RDS).
- **Docker** – Contenerización para despliegue consistente.
- **Swagger UI** – Documentación automática OpenAPI 3.1.

---

## 📚 Endpoints principales

### 🧍 Customers
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET    | `/customers` | Listar clientes |
| POST   | `/customers` | Crear cliente |
| GET    | `/customers/{id}` | Obtener cliente por ID |
| PATCH  | `/customers/{id}` | Actualizar cliente |
| DELETE | `/customers/{id}` | Eliminar cliente |
| POST   | `/customers/{id}/plans/{plan_id}` | Suscribir cliente a plan |
| GET    | `/customers/{id}/plans` | Listar planes de un cliente |

### 💳 Transactions
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET    | `/transactions` | Listar transacciones |
| POST   | `/transactions` | Crear transacción |

### 📦 Plans
| Método | Ruta | Descripción |
|--------|------|-------------|
| GET    | `/plans` | Listar planes |
| POST   | `/plans` | Crear plan |

---

## 🧪 Ejecutar localmente

```bash
# Clona el repositorio
git clone https://github.com/tuusuario/mi-primera-api.git
cd mi-primera-api

# Crea un entorno virtual
python -m venv .venv
source .venv/bin/activate  # en Linux/macOS
.venv\Scripts\activate     # en Windows

# Instala dependencias
pip install -r requirements.txt

# Ejecuta la API
uvicorn app.main:app --reload
