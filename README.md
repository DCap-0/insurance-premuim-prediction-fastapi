# Insurance Premium Prediction – FastAPI

End-to-end machine learning application for predicting insurance premiums, built using **FastAPI** for the backend and a lightweight **Python frontend**.

<!-- --- -->

## Project Structure

  ```
  insurance-premuim-prediction-fastapi/
  │
  ├── backend/          # FastAPI backend + ML model
  ├── frontend/         # Simple frontend client
  ├── data/             # Dataset used for training
  ├── docker/           # Docker & docker-compose setup
  ├── notebooks/        # Experiments & model training
  ├── LICENSE
  └── README.md
  ```

<!-- --- -->

## Architecture Overview

- **Backend**
  - FastAPI application
  - Loads a trained ML model (`model.pkl`)
  - Exposes REST APIs for prediction and health checks
- **Frontend**
  - Python-based client to interact with backend
- **Docker**
  - Containerized setup for backend and frontend

<!-- --- -->

## Running with Docker (Recommended)

  ```bash
  docker compose -f docker/docker-compose.yaml up --build
  ```

Backend will be available at: [http://localhost:8000](http://localhost:8000)

API Docs:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

<!-- --- -->

## Running Locally (Without Docker)

See:
- `backend/README.md`
- `frontend/README.md`

<!-- --- -->

## Tech Stack

- FastAPI
- Pydantic
- Steamlit
- Docker & Docker Compose
- Python 3.12

<!-- --- -->

## License

This project is licensed under the MIT License.
