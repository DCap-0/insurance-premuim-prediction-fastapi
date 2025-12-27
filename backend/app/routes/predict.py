from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schema.user_input import UserInput
from app.schema.prediction_response import PredictionResponse
from model.predict import predict_output

router = APIRouter(
    prefix='/predict',
    tags=['ml', 'POST']
)


@router.post('', response_model=PredictionResponse)
def predict_premium(data: UserInput):
    # return data

    user_input = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code=200, content={'response': prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
