from fastapi import APIRouter
from typing import List

# Models
from api.models.user_models import User

# Controllers
from api.controllers.user_controller import (
    add_user,
    get_all_users,
    get_user_by_id,
    update_user_by_id,
    delete_user_by_id,
)

router = APIRouter(prefix="/users", tags=["User"])

router.post("/", response_model=User)(add_user)
router.get("/", response_model=List[User])(get_all_users)
router.get("/{user_id}", response_model=User)(get_user_by_id)
router.patch("/{user_id}", response_model=User)(update_user_by_id)
router.delete("/{user_id}", response_model=None)(delete_user_by_id)
