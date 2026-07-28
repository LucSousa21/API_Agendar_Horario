from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.cliente import Cliente
from app.schemas.cliente import CadastrarCliente, ClienteResponse


# Cria um agrupador de rotas
# Todas as rotas desse arquivo serão registradas através desse router
router = APIRouter()


# ==========================================================
# GET - Listar todos os clientes
# Endpoint: GET /clientes
# ==========================================================

@router.get("/clientes", response_model=list[ClienteResponse])
def listar_clientes(
    db: Session = Depends(get_db)
):
    """
    Busca todos os clientes cadastrados no banco.
    """

    # Faz uma consulta na tabela Cliente
    # SQL equivalente:
    # SELECT * FROM clientes;
    clientes = db.query(Cliente).all()

    # Retorna uma lista de clientes
    return clientes



# ==========================================================
# POST - Criar um novo cliente
# Endpoint: POST /clientes
# ==========================================================

@router.post("/clientes", response_model=ClienteResponse)
def criar_cliente(
    cliente: CadastrarCliente,
    db: Session = Depends(get_db)
):
    """
    Recebe os dados de um cliente,
    cria um registro no banco e retorna o cliente criado.
    """


    # Cria um objeto Cliente utilizando os dados recebidos
    novo_cliente = Cliente(
        nome=cliente.nome,
        telefone=cliente.telefone,
        email=cliente.email
    )


    # Adiciona o objeto na sessão do banco
    db.add(novo_cliente)


    # Confirma a gravação no banco
    db.commit()


    # Atualiza o objeto com dados gerados pelo banco
    # Exemplo: ID criado automaticamente
    db.refresh(novo_cliente)


    # Retorna o cliente criado
    return novo_cliente



# ==========================================================
# PUT - Atualizar um cliente existente
# Endpoint: PUT /clientes/{cliente_id}
# ==========================================================

@router.put("/clientes/{cliente_id}", response_model=ClienteResponse)
def atualizar_cliente(
    cliente_id: int,
    cliente: CadastrarCliente,
    db: Session = Depends(get_db)
):
    """
    Localiza um cliente pelo ID e atualiza seus dados.
    """


    # Busca o cliente pelo ID informado
    # SQL equivalente:
    # SELECT * FROM clientes WHERE cliente_id = cliente_id;
    cliente_db = (
        db.query(Cliente)
        .filter(Cliente.cliente_id == cliente_id)
        .first()
    )


    # Caso não encontre o cliente
    if cliente_db is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )


    # Atualiza os campos do cliente encontrado
    cliente_db.nome = cliente.nome
    cliente_db.telefone = cliente.telefone
    cliente_db.email = cliente.email


    # Salva as alterações
    db.commit()


    # Atualiza o objeto com os dados atuais do banco
    db.refresh(cliente_db)


    return cliente_db



# ==========================================================
# DELETE - Deletar um cliente
# Endpoint: DELETE /clientes/{cliente_id}
# ==========================================================

@router.delete("/clientes/{cliente_id}")
def deletar_cliente(
    cliente_id: int,
    db: Session = Depends(get_db)
):
    """
    Remove um cliente do banco pelo ID.
    """


    # Busca o cliente que será removido
    cliente = (
        db.query(Cliente)
        .filter(Cliente.cliente_id == cliente_id)
        .first()
    )


    # Verifica se o cliente existe
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )


    # Remove o registro encontrado
    db.delete(cliente)


    # Confirma a exclusão no banco
    db.commit()


    return {
        "message": "Cliente deletado com sucesso."
    }
