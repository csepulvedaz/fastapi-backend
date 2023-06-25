from fastapi import status
from api.models.error_models import ErrorResponse, ErrorMessage

# User errors messages
USER_CREATE_ERROR = ErrorResponse(
    message=ErrorMessage(es="Error creando usuario", en="Error creating user"),
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
)
USERS_GETTING_ERROR = ErrorResponse(
    message=ErrorMessage(es="Error obteniendo usuarios", en="Error getting users"),
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
)

USER_GETTING_ERROR = ErrorResponse(
    message=ErrorMessage(es="Error obteniendo usuario", en="Error getting user"),
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
)
USER_UPDATING_ERROR = ErrorResponse(
    message=ErrorMessage(es="Error actualizando usuario", en="Error updating user"),
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
)
USER_DELETING_ERROR = ErrorResponse(
    message=ErrorMessage(es="Error eliminando usuario", en="Error deleting user"),
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
)

# Auth errors messages
INVALID_CREDENTIALS_ERROR = ErrorResponse(
    message=ErrorMessage(es="Usuario o password incorrectos", en="Incorrect username or password"),
    status_code=status.HTTP_401_UNAUTHORIZED,
)
INVALID_TOKEN_ERROR = ErrorResponse(
    message=ErrorMessage(
        es="Credenciales de autentiación inválidas",
        en="Invalid authentication credentials",
    ),
    status_code=status.HTTP_401_UNAUTHORIZED,
    headers={"WWW-Authenticate": "Bearer"},
)

# Data validation errors messages
INVALID_EMAIL_ERROR = ErrorResponse(
    message=ErrorMessage(es="Email inválido", en="Invalid email"),
    status_code=status.HTTP_400_BAD_REQUEST,
)
VALIDATION_ERROR = ErrorResponse(
    message=ErrorMessage(
        es="Faltan uno o más campos o son erróneos",
        en="One or more fields are missing or wrong",
    ),
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
)
