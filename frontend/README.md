# Frontend – Insurance Premium Predictor (Streamlit)

This is the **frontend application** for the Insurance Premium Prediction system.  
It is built using **Streamlit** and communicates with the FastAPI backend via HTTP requests.

<!-- --- -->

## Tech Stack

- Python 3.10+
- Streamlit
- Requests
- FastAPI (backend dependency)

<!-- --- -->

## Features

- Interactive UI for user input
- Sends user data to FastAPI `/predict` endpoint
- Displays:
  - Predicted premium category
  - Confidence score
  - Class-wise probability distribution
- Graceful handling of backend connection errors

<!-- --- -->

## Project Structure

  ```text
  frontend/
  ├── app.py
  ├── Dockerfile
  ├── README.md
  └── requirements.txt
  ```

<!-- --- -->

## Backend Dependency

- The frontend depends on the FastAPI backend running locally.
- Expected backend endpoint: [localhost:8000/predict](http://localhost:8000/predict)
- Make sure the backend server is running before starting the frontend.

<!-- --- -->

## Environment Configuration

The frontend supports both `.env` files and Streamlit Secrets with a fallback mechanism.

### Priority Order

1. `st.secrets` (Streamlit Cloud)
2. Environment variables (`.env` or OS)
3. Application exits with an explicit error

### Local Development (`.env`)

Create a `.env` file inside the `frontend/` directory:

  ```env
  API_URL=http://localhost:8000/predict
  ```

<!-- --- -->

## Input Fields

The Streamlit UI collects the following user inputs:

- **Age** – Integer value (0–120)
- **Weight (kg)** – Float value
- **Height (meters)** – Float value
- **Income (LPA)** – Annual income in lakhs per annum
- **Smoking Status** – Selected as *Yes* or *No* (converted to boolean)
- **City** – Text input representing the user’s city
- **Occupation** – Selected from the following options:
  - `retired`
  - `freelancer`
  - `student`
  - `government_job`
  - `business_owner`
  - `unemployed`
  - `private_job`

These inputs are sent as JSON to the backend.

<!-- --- -->

## API Request Format

  ```json
  {
    "age": 30,
    "weight": 45.5,
    "height": 1.5,
    "income_lpa": 10.0,
    "smoker": false,
    "city": "Delhi",
    "occupation": "private_job"
  }
  ```

<!-- --- -->

## API Response Handling

On successful prediction, the frontend expects a response structure like:

  ```json
  {
    "response": {
      "predicted_category": "Medium",
      "confidence": 0.87,
      "class_probabilities": {
        "Low": 0.05,
        "Medium": 0.87,
        "High": 0.08
      }
    }
  }
  ```
The UI displays:
- Predicted category
- Confidence score
- Full probability distribution

<!-- --- -->

## Running the Frontend Locally

1. Create a virtual environment (optional but recommended)
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

2. Install dependencies
  ```bash
  pip install -r requirements.txt
  ```

3. Start the Streamlit app
  ```bash
  streamlit run app.py
  ```

<!-- --- -->

## Access the App

Once running, open your browser at: [localhost:8501](http://localhost:8501)

<!-- --- -->

## Common Errors & Fixes

### Backend not running

If you see: 
  ```bash
  Could not connect to the FastAPI server
  ```

Make sure:
- Backend is running on `http://localhost:8000`
- `/predict` endpoint is available