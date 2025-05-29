from src.domain.dtos import ActiviesDTO,UpdateActivitieDTO
from src.domain.entities import ActiviesEntity
from src.repositories import ActiviesRepository


class ActiviesService:
    def __init__(self) -> None:
        self.activies_repository = ActiviesRepository()

    def get_activies(self) -> list:
        return self.activies_repository.get_activies()

    def create_activie(self, dto: ActiviesDTO) -> dict:
        activie_exists = self.activies_repository.get_activie(dto.name)

        if activie_exists:
            raise ValueError("Atividade ja cadastrada")
        print(dto)
        entity = ActiviesEntity.create(dto)
        return self.activies_repository.create(entity)

    def update_activie(self, dto: UpdateActivitieDTO, id: int) -> dict:
        activie_exists = self.activies_repository.get_activie_by_id(id)

        if not activie_exists:
            raise ValueError("Atividade não encontrada")

        entity = ActiviesEntity.create(dto)
        return self.activies_repository.update(entity, id)

    def delete_activie(self, id: int) -> dict:
        return self.activies_repository.delete(id)

    def total_activie(self):
        return self.activies_repository.count()