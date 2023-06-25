from datetime import timedelta
import email_validator
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

# Services
from api.services.user_services import get_user_by_email

# Constants
from api.constants.auth_constants import ACCESS_TOKEN_EXPIRE_WEEKS

# Models
from api.models.auth_models import Token

# Utils
from api.utils.auth_utils import (
    authenticate_user,
    create_access_token,
)


async def signin(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validate email
    try:
        email_validator.validate_email(form_data.username)
    except email_validator.EmailNotValidError as e:
        raise e

    user = await get_user_by_email(form_data.username)
    authenticated_user = authenticate_user(user, form_data.password)

    if not authenticated_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(weeks=ACCESS_TOKEN_EXPIRE_WEEKS)
    access_token = create_access_token(
        data={"sub": authenticated_user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="Bearer")
