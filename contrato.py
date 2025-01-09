from pydantic import BaseModel,validator, Field
from datetime import datetime
from decimal import Decimal
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
    meta: Decimal = Field(..., ge=0, description="Meta deve ser maior ou igual a 0") 
    piso_remuneracao: Decimal = Field(..., ge=0, description="O valor do piso deve ser maior ou igual a 0") 

class Funcionarios(BaseModel):
    """
    Validação dos dados de entrada da tela de cadastros de funcionário.

    Args:
        nomeÇ nome do funcionário
        login: login do funcionário
        grupo: grupo que o funcionário faz parte
        vinculo: vinculo do funcionário
        dt_inicio: data de início da meta 
        dt_fim: data de fim da meta
    
    """

    nome: str
    login: str
    grupo: str
    vinculo: str
    dt_inicio: datetime
    dt_fim: datetime
