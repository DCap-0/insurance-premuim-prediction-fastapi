from .home import router as home_router
from .health import router as health_router
from .predict import router as predict_router


all_routers = [
    home_router,
    health_router,
    predict_router
]
