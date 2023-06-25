from fastapi import APIRouter

# Models
from api.models.auth_models import Token

# Controllers
from api.controllers.auth_controller import signin


router = APIRouter(prefix="/auth", tags=["Auth"])

router.post("/signin", response_model=Token)(signin)
