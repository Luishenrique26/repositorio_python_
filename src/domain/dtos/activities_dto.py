from datetime import date, datetime
from pydantic import BaseModel, field_validator
from typing import Optional
from src.common.utils import str_to_date


class ActivitiesDTO(BaseModel):
    name: str
    description: Optional[str]
    start_date: date
    end_date: date

    @field_validator("name", mode="before")
    def validate_name(cls, value: str) -> str:
        if not value or value.strip() == "":
            raise ValueError("Campo de nome de atividade é obrigatório")

        return value

    @field_validator("start_date", mode="before")
    def validate_start_date(cls, value: date) -> date:
        if isinstance(value, str):
            if not value:
                raise ValueError("Campo de data de início é obrigatório")

            if len(value) != 10:
                raise ValueError("Campo de data de início é inválido")

            try:
                return str_to_date(value, "%d/%m/%Y")
            except ValueError:
                raise ValueError("Campo de data de início é inválido")

        return value

    @field_validator("end_date", mode="before")
    def validate_end_date(cls, value: date) -> date:
        if isinstance(value, str):
            if not value:
                raise ValueError("Campo de data de fim é obrigatório")

            if len(value) != 10:
                raise ValueError("Campo de data de fim é inválido")

            try:
                return str_to_date(value, "%d/%m/%Y")
            except ValueError:
                raise ValueError("Campo de data de fim é inválido")

        return value


class UpdateActivitieDTO(ActivitiesDTO):
    activitie_id: int
    #created_at: datetime

    # @field_validator("created_at", mode="before")
    # def validate_created_at(cls, value: datetime) -> datetime:
    #     if isinstance(value, str):
    #         if not value:
    #             raise ValueError("Campo de data de criação é obrigatório")

    #         if len(value) != 19:
    #             raise ValueError("Campo de data de criação é inválido")

    #         try:
    #             return str_to_datetime(value, "%Y-%m-%d - %H:%M:%S.%f")
    #         except ValueError:
    #             raise ValueError("Campo de data de criação é inválido")

    #    return value
