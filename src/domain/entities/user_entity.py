from datetime import datetime
from src.domain.dtos.user_dto import UserDTO


class UserEntity:
    user_id: int
    username: str
    email: str
    password: str
    created_at: str

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    @staticmethod
    def create(dto: UserDTO) -> 'UserEntity':
        return UserEntity(username=dto.username, email=dto.email, password=dto.password)
