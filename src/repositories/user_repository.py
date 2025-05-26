from database.config import conection_db
from src.domain.entities import UserEntity


class UserRepository:
    def get_user(self, username: str) -> dict | None:
        with conection_db() as cursor:
            query = cursor.execute(
                """
                SELECT * FROM users WHERE username = ?
            """,
                (username,),
            ).fetchone()
            print(query)
        return (
            None
            if not query
            else {
                "user_id": query[0],
                "username": query[1],
                "email": query[2],
                "password": query[3],
                "created_at": query[4],
            }
        )

    def get_user_by_email(self, email: str) -> dict | None:
        with conection_db() as cursor:
            query = cursor.execute(
                """
                SELECT * FROM users WHERE email = ?
            """,
                (email,),
            ).fetchone()
            print(query)
        return (
            None
            if not query
            else {
                "user_id": query[0],
                "username": query[1],
                "email": query[2],
                "password": query[3],
                "created_at": query[4],
            }
        )
    
    def create(self, entity: UserEntity) -> dict:
        with conection_db() as cursor:
            query = cursor.execute(
                """
                INSERT INTO users (username, email, password, created_at) VALUES (?, ?, ?, ?)
                RETURNING *
            """,
                (entity.username, entity.email, entity.password, entity.created_at),
            ).fetchone()
        return {
            "user_id": query[0],
            "username": query[1],
            "email": query[2],
            "password": query[3],
            "created_at": query[4],
        }
