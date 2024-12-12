from pydantic import BaseModel,validator, PositiveFloat, PositiveInt
from datetime import datetime
from enum import Enum
from typing import Optional

class Metas(BaseModel):
    """
    Validação dos dados de entrada da tela de Metas cadastradas.

    Args:
        login: login do funcionário
        dt_inicio: data de início da meta 
        dt_fim: data de fim da meta
        meta: valor da meta 
    """

    login: str
    dt_inicio: datetime
    dt_fim: datetime
    meta: PositiveInt
    piso_remuneracao: PositiveFloat