from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
import phonenumbers

class Cliente(BaseModel):
    nome_cliente: str
    telefone_cliente: str
    email_cliente: EmailStr
    @field_validator("telefone_cliente")
    @classmethod
    def validar_telefone(cls, value):
        try:
            numero = phonenumbers.parse(value, "BR")
            if not phonenumbers.is_valid_number(numero):
                raise ValueError("Telefone inválido")
        except:
            raise ValueError("Telefone inválido")

        return value