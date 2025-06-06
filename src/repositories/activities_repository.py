from database.config import conection_db
from src.domain.entities import ActivitiesEntity


class ActivitiesRepository:
    def get_activities(self):
        with conection_db() as cursor:
            query = cursor.execute(
                """
                SELECT * FROM activities
            """
            ).fetchall()
        return (
            None 
            if not query 
            else [
                {
                    "activitie_id": x[0],
                    "name": x[1],
                    "description": x[2],
                    "start_date": x[3],
                    "end_date": x[4],
                    "created_at": x[5],
                    "updated_at": x[6],
                } 
                for x in query 
            ]
        )        

    def get_activitie(self, name: str):
        with conection_db() as cursor:
            query = cursor.execute(
                """
                SELECT * FROM activities WHERE name = ?
            """,
                (name,),
            ).fetchone()
        return (
            None
            if not query
            else {
                "activitie_id": query[0],
                "name": query[1],
                "decription": query[2],
                "start_date": query[3],
                "end_date": query[4],
                "created_at": query[5],
                "updated_at": query[6],
            }
        )

    def get_activitie_by_id(self, id: int):
        with conection_db() as cursor:
            query = cursor.execute(
                """
                SELECT * FROM activities WHERE activitie_id = ?
            """,
                (id,),
            ).fetchone()
        return (
            None
            if not query
            else {
                "activitie_id": query[0],
                "name": query[1],
                "decription": query[2],
                "start_date": query[3],
                "end_date": query[4],
                "created_at": query[5],
                "updated_at": query[6],
            }
        )
    
    def create(self, entity: ActivitiesEntity) -> dict:
        with conection_db() as cursor:
            query = cursor.execute(
                """
                INSERT INTO activities (name, description, start_date, end_date, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)
                RETURNING *
            """,
                (
                    entity.name,
                    entity.description,
                    entity.start_date,
                    entity.end_date,
                    entity.created_at,
                    entity.updated_at,
                ),
            ).fetchone()
        return {
                "activitie_id": query[0],
                "name": query[1],
                "description": query[2],
                "start_date": query[3],
                "end_date": query[4],
                "created_at": query[5],
                "updated_at": query[6],
            }

    def update(self, entity: ActivitiesEntity, id: int) -> dict:
        with conection_db() as cursor:
            query = cursor.execute(
                """
                UPDATE activities SET name = ?, description = ?, start_date = ?, end_date = ?, updated_at = ? WHERE activitie_id = ?
                RETURNING *
            """,
                (
                    entity.name,
                    entity.description,
                    entity.start_date,
                    entity.end_date,
                    entity.updated_at,
                    id,
                ),
            ).fetchone()
        return {
                "activitie_id": query[0],
                "name": query[1],
                "decription": query[2],
                "start_date": query[3],
                "end_date": query[4],
                "created_at": query[5],
                "updated_at": query[6],
            }

    def delete(self, id: int):
        with conection_db() as cursor:
            query = cursor.execute(
                """
                DELETE FROM activities WHERE activitie_id = ?
                RETURNING *
            """,
                (id,),
            ).fetchone()
        return query

    
    def count(self):
        with conection_db() as cursor:
            query = cursor.execute(
                """
                SELECT COUNT(*) FROM activities
            """
            ).fetchone()
        return query
