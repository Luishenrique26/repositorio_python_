from src.repositories import UserRepository
from bcrypt import checkpw


class AuthService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def login(self, username: str, password: str) -> dict | None:
        user = self.user_repository.get_user(username)
        if not user:
            raise ValueError("Usuário não encontrado")

        if not checkpw(password.encode("utf-8"), user["password"].encode()):
            raise ValueError("Senha inválida")

        return user
