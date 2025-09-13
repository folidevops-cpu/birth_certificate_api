# Birth Certificate API

## Overview
This API allows you to manage birth certificate records, including creating, retrieving, and listing certificates, children, and parent information. It is built with FastAPI and uses SQLAlchemy for database operations.

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
3. (Optional) Seed the database with fake data:
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
- `POST /birth-certificate/` — Create a birth certificate (with child, father, mother info)
- `GET /birth-certificate/{registration_number}` — Get a birth certificate by registration number
- `GET /birth-certificates/` — List birth certificates (paginated)

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
    models/
        database_models.py
        models.py
```

## License
MIT
