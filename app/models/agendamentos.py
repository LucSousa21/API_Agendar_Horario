from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database.database import Base


class Agendamento(Base):
    __tablename__ = "agendamentos"

    id_agendamento = Column(Integer, primary_key=True, index=True)

    id_cliente = Column(
        Integer,
        ForeignKey("clientes.id_cliente"),
        nullable=False
    )

    id_horario = Column(
        Integer,
        ForeignKey("horarios.id_horario"),
        nullable=False
    )

    status = Column(
        String,
        default="confirmado",
        nullable=False
    )

    criado_em = Column(
        DateTime,
        server_default=func.now()
    )