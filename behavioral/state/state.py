from __future__ import annotations
from abc import ABC, abstractmethod

# Classe contexto, semáforo
class Semaforo:
    _estado = None
    
    def __init__(self) -> None:
        self._estado = Vermelho()

    @property
    def estado(self) -> Estado:
        return self._estado

    @estado.setter
    def estado(self, novo_estado: Estado) -> None:
        self._estado = novo_estado

    def mudar(self) -> None:
        self._estado.proximo(self)

# Classe abstrata de estado
# Estados -> Verde, Amarelo e Vermelho
class Estado(ABC):
    @abstractmethod
    def proximo(self, semaforo: Semaforo) -> None: pass

# Classes de estados concretas
class Verde(Estado):
    def proximo(self, semaforo: Semaforo) -> None:
        print("Fim do estado Verde. Mudando para Amarelo")
        semaforo.estado = Amarelo()

class Amarelo(Estado):
    def proximo(self, semaforo: Semaforo) -> None:
        print("Fim do estado Amarelo. Mudando para Vermelho")
        semaforo.estado = Vermelho()

class Vermelho(Estado):
    def proximo(self, semaforo: Semaforo) -> None:
        print("Fim do estado Vermelho. Mudando para Verde")
        semaforo.estado = Verde()

# Implementação
s = Semaforo()

print("Estado atual:", s.estado.__class__.__name__) # Estado de inicialização => Vermelho

s.mudar() # Vermelho -> Verde
s.mudar() # Verde -> Amarelo
s.mudar() # Amarelo -> Vermelho
