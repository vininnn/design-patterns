from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

# Enum com os tipos de pagamento
# Não entra necessariamente para a construção de uma factory
class TipoPagamento(Enum):
    PIX = "pix"
    CARTAO = "cartao"
    BOLETO = "boleto"

# Classe fábrica, fábrica de pagamentos
# Fábrica responsável por instanciar os tipos de pagamento
class FabricaPagamentos():
    def __init__(self):
        pass

    def criar_pagamento(self, tipo_pagamento: TipoPagamento) -> Pagamento:
        if tipo_pagamento == TipoPagamento.PIX:
            return PagamentoPix()
        
        if tipo_pagamento == TipoPagamento.CARTAO:
            return PagamentoCartao()
        
        if tipo_pagamento == TipoPagamento.BOLETO:
            return PagamentoBoleto()
        
        raise ValueError(f"Tipo de pagamento inválido: {tipo_pagamento}")

# Produtos
class Pagamento(ABC):
    @abstractmethod
    def realizar_pagamento(self, valor: float) -> None: pass

# Produtos concretos
class PagamentoPix(Pagamento):
    def realizar_pagamento(self, valor: float) -> None:
        print(f"R${valor:.2f} pago via Pix")

class PagamentoCartao(Pagamento):
    def realizar_pagamento(self, valor: float) -> None:
        print(f"R${valor:.2f} pago via Cartão")

class PagamentoBoleto(Pagamento):
    def realizar_pagamento(self, valor: float) -> None:
        print(f"R${valor:.2f} pago via Boleto")

# Implementação
fabrica = FabricaPagamentos()

pagamento = fabrica.criar_pagamento(TipoPagamento.PIX)
pagamento.realizar_pagamento(50)

pagamento = fabrica.criar_pagamento(TipoPagamento.CARTAO)
pagamento.realizar_pagamento(200.5)

pagamento = fabrica.criar_pagamento(TipoPagamento.BOLETO)
pagamento.realizar_pagamento(997.99)
