from .root_routes import router as root_routes
from .user_routes import router as user_routes
from .auth_routes import router as auth_routes


__all__ = ["root_routes", "user_routes", "auth_routes"]
