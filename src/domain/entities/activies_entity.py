from datetime import datetime
from src.domain.dtos import ActiviesDTO
from datetime import datetime, date
from typing import Optional

class ActiviesEntity:
    def __init__(
        self,
        name: str,
        description: Optional[str],
        start_date: date,
        end_date: date,
    ) -> None:
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @staticmethod
    def create(dto: ActiviesDTO) -> "ActiviesEntity":
        return ActiviesEntity(dto.name,dto.description, dto.start_date, dto.end_date)
