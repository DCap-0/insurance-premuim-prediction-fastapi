# Backend – FastAPI Insurance Premium Prediction

FastAPI backend serving an ML model for insurance premium prediction.

<!-- --- -->

## Folder Structure

  ```
  backend/
  │
  ├── app/
  │   ├── main.py          # FastAPI app entry point
  │   ├── routes/          # API routes
  │   │   ├── home.py
  │   │   ├── health.py
  │   │   └── predict.py
  │   ├── schema/          # Pydantic models
  │   └── utils/           # Helper utilities
  │
  ├── model/
  │   ├── model.pkl        # Trained ML model
  │   └── predict.py
  │
  ├── Dockerfile
  ├── requirements.txt
  ├── requirements-lock.txt
  └── README.md
  ```

<!-- --- -->

## API Endpoints

1. Home: ` GET / `
2. Health Check: ` GET /health `
3. Prediction: ` POST /predict `

<!-- --- -->

## Sample Prediction Request

  ```json
  {
    "age": 35,
    "bmi": 27.5,
    "children": 2,
    "smoker": "no",
    "region": "northwest",
    "city": "Delhi"
  }
  ```

<!-- --- -->

## Run Locally

### 1. Create virtual environment
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### 2. Install dependencies
  ```bash
  pip install -r requirements.txt
  ```

### 3. Start server
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
  ```

Backend will be available at: [http://localhost:8000](http://localhost:8000)

<!-- --- -->

## API Documentation

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

<!-- --- -->

