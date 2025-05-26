import re
from pydantic import BaseModel, EmailStr, model_validator, field_validator


class UserDTO(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator("username", mode="before")
    def validate_username(cls, value: str) -> str:
        if not value or value.strip() == "":
            raise ValueError("Campo de nome de usuário obrigatório")

        return value

    @field_validator("email", mode="before")
    def validate_email(cls, value: EmailStr) -> EmailStr:
        if not value or value.strip() == "":
            raise ValueError("Campo de email obrigatório")

        if re.match(r"^\S+@\S+\.\S+$", value) is None:
            raise ValueError("Campo de email inválido")

        return value

    @field_validator("password", mode="before")
    def validate_password(cls, value: str) -> str:
        if not value or value.strip() == "":
            raise ValueError("Campo de senha obrigatória")

        if len(value) < 8:
            raise ValueError("O campo de senha deve ter pelo menos 8 caracteres")

        return value

    @model_validator(mode="after")
    def validate(self) -> "UserDTO":
        if self.username == self.password:
            raise ValueError(
                "O campo de senha deve ser diferente do campo de nome de usuário"
            )

        return self
