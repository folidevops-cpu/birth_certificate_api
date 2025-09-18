# Birth Certificate API

## Overview
This API allows you to manage birth certificate records, including creating, retrieving, and listing certificates, children, and parent information. It is built with FastAPI and uses SQLAlchemy for database operations.

### Features
- Birth certificate CRUD operations
- Role-based authentication (JWT)
- Test users for development
- Integration-ready for modern frontend (Vue)

## Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd birth_certificate_api
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Seed the database with fake data and test users:
   ```bash
   python app/seed_data.py
   ```

### Running the App
Start the server with:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
Or using the virtual environment:
```bash
venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API Endpoints


### Endpoints
- `POST /token` — Login and get JWT token
- `POST /users/` — Create a new user (Registry Office role required)
- `GET /profile` — Get current user profile (requires JWT)
- `POST /logout` — Logout user (frontend only, clears token)
- `POST /birth-certificate/` — Create a birth certificate (with child, father, mother info)
- `GET /birth-certificate/{registration_number}` — Get a birth certificate by registration number
- `GET /birth-certificates/` — List birth certificates (paginated)

## Authentication & Test Users
The API uses JWT authentication. After seeding, you can use these test users:

- **hospital_user** / `hospital123` (role: hospital)
- **registry_user** / `registry123` (role: registry_office)
- **police_user** / `police123` (role: police)

## API Documentation
Interactive API docs are available at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Project Structure
```
requirements.txt
app/
   database.py
   main.py
   seed_data.py
   test_db.py
   auth/
      auth.py
      crud.py
      models.py
      schemas.py
   models/
      database_models.py
      models.py
```

## Frontend Integration
You can connect this API to a Vue frontend (see birth-certificate-frontend) for a complete birth certificate management system. Proxy `/token`, `/birth-certificate`, and `/birth-certificates` endpoints for seamless integration.

## License
MIT
