from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        schema_extra = {"example": {"access_token": "abcdefg123456", "token_type": "bearer"}}
