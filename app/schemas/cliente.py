from pydantic import BaseModel, EmailStr, field_validator
import phonenumbers


# Classe responsável pelos dados de entrada do cadastro.
class CadastrarCliente(BaseModel):
    nome: str
    telefone: str
    email: EmailStr

    @field_validator("telefone")
    @classmethod
    def validar_telefone(cls, value):
        try:
            numero = phonenumbers.parse(value, "BR")

            if not phonenumbers.is_valid_number(numero):
                raise ValueError("Telefone inválido")

        except:
            raise ValueError("Telefone inválido")

        return value



# Classe responsável pelo formato da resposta da API.
class ClienteResponse(BaseModel):
    cliente_id: int
    nome: str
    telefone: str
    email: EmailStr

    class Config:
        from_attributes = True
