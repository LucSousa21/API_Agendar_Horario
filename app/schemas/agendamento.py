from pydantic import BaseModel
from datetime import datetime


# Entrada: cliente envia para criar o agendamento
class AgendamentoCreate(BaseModel):
    id_cliente: int
    id_horario: int


# Saída: administrador
class AgendamentoAdminResponse(BaseModel):
    id_agendamento: int
    id_cliente: int
    id_horario: int
    status: str
    criado_em: datetime

    class Config:
        from_attributes = True


# Saída: cliente
class AgendamentoClienteResponse(BaseModel):
    id_agendamento: int
    data_agendada: datetime
    status: str

    class Config:
        from_attributes = True