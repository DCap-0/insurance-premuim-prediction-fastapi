from fastapi import APIRouter

router = APIRouter(
    prefix='',
    tags=['general', 'GET']
)


@router.get('/')
def home() -> None:
    return {'message': 'Insurance Premium Prediction API'}
