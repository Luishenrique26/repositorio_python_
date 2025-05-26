from pydantic import BaseModel, field_validator


class LoginDTO(BaseModel):
    username: str
    password: str

    @field_validator("username")
    def validate_username(cls, value: str) -> str:
        if not value or value.strip() == "":
            raise ValueError("Campo de nome de usuário obrigatório")

        return value

    @field_validator("password")
    def validate_password(cls, value: str) -> str:
        if not value or value.strip() == "":
            raise ValueError("Campo de senha obrigatória")

        return value
