from src.repositories import UserRepository
from src.domain.entities import UserEntity
from src.domain.dtos import UserDTO
from bcrypt import gensalt, hashpw
from random import randint


class UserService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()

    def create_user(self, dto: UserDTO) -> dict:
        user_exists = self.user_repository.get_user_by_email(dto.email)

        if user_exists:
            raise ValueError("Usuário já cadastrado")

        dto.password = hashpw(
            dto.password.encode(), gensalt(rounds=randint(10, 14))
        ).decode()
        entity = UserEntity.create(dto)
        return self.user_repository.create(entity)
