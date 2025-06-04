from src.domain.dtos import ActivitiesDTO,UpdateActivitieDTO
from src.domain.entities import ActivitiesEntity
from src.repositories import ActivitiesRepository


class ActivitiesService:
    def __init__(self) -> None:
        self.activities_repository = ActivitiesRepository()

    def get_activities(self) -> list:
        return self.activities_repository.get_activities()

    def create_activitie(self, dto: ActivitiesDTO) -> dict:
        activie_exists = self.activities_repository.get_activitie(dto.name)

        if activie_exists:
            raise ValueError("Atividade ja cadastrada")
        print(dto)
        entity = ActivitiesEntity.create(dto)
        return self.activities_repository.create(entity)

    def update_activitie(self, dto: UpdateActivitieDTO, id: int) -> dict:
        activitie_exists = self.activities_repository.get_activitie_by_id(id)

        if not activitie_exists:
            raise ValueError("Atividade não encontrada")

        entity = ActivitiesEntity.create(dto)
        return self.activities_repository.update(entity, id)

    def delete_activitie(self, id: int) -> dict:
        return self.activities_repository.delete(id)

    def total_activitie(self):
        return self.activities_repository.count()