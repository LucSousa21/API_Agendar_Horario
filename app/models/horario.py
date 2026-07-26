from sqlalchemy import Column, Integer, DateTime, Boolean
from app.database.database import Base


class Horario(Base):
    __tablename__ = "horarios"

    id_horario = Column(Integer, primary_key=True, index=True)
    data_horario = Column(DateTime, nullable=False)
    disponivel = Column(Boolean, default=True, nullable=False)