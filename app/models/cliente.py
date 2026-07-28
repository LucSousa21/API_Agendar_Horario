from sqlalchemy import Column, Integer, String
from app.database.database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    cliente_id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False)