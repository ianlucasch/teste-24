from enum import Enum
from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt

class ProdutoEnum(str, Enum):
    produto1 = "Gemini"
    produto2 = "chatGPT"
    produto3 = "Llama 3.0"

class Vendas(BaseModel):
    """
    Modelo de dados para vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum