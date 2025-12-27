from fastapi import APIRouter
from model.predict import model, MODEL_VERSION

router = APIRouter(
    prefix='/health',
    tags=['general', 'GET']
)


@router.get('')
def health_check() -> dict:
    return {
        'status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }
