from __future__ import annotations
from abc import ABC, abstractmethod

# Produto
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

# Criador
class ProcessadorPagamento(ABC):
    @abstractmethod
    def criar_pagamento(self) -> Pagamento: pass

    def processar_pagamento(self, valor: float) -> None:
        print("Iniciando processamento...")

        pagamento = self.criar_pagamento()

        pagamento.realizar_pagamento(valor)

        print("Pagamento processado com sucesso.")

# Criadores concretos
class ProcessadorPix(ProcessadorPagamento):
    def criar_pagamento(self) -> Pagamento:
        return PagamentoPix()

class ProcessadorCartao(ProcessadorPagamento):
    def criar_pagamento(self) -> Pagamento:
        return PagamentoCartao()

class ProcessadorBoleto(ProcessadorPagamento):
    def criar_pagamento(self) -> Pagamento:
        return PagamentoBoleto()

# Implementação
processador = ProcessadorPix()
processador.processar_pagamento(50)

processador = ProcessadorCartao()
processador.processar_pagamento(200.5)

processador = ProcessadorBoleto()
processador.processar_pagamento(997.99)