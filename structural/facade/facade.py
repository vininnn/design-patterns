# Classe fachada(facade), calculadora
class CalculadoraFachada():
    def __init__(self):
        self.probabilidade = Probabilidade()
        self.combinatoria = Combinatoria()

    def probabilidade_simples(self, casos_favoraveis: int, total_casos: int) -> float:
        return self.probabilidade.simples(casos_favoraveis, total_casos)

    def probabilidade_condicional(self, a_intersecao_b: float, probabilidade_a: int) -> float:
        return self.probabilidade.condicional(a_intersecao_b, probabilidade_a)

    def complementar(self, probabilidade_a: float) -> float:
        return self.probabilidade.complementar(probabilidade_a)
    
    def uniao(self, probabilidade_a: float, probabilidade_b: float, pa_intersecao_b: float) -> float:
        return self.probabilidade.uniao(probabilidade_a, probabilidade_b, pa_intersecao_b)
    
    def intersecao_independente(self, probabilidade_a: float, probabilidade_b: float) -> float:
        return self.probabilidade.intersecao_independente(probabilidade_a, probabilidade_b)
    
    def intersecao_dependente(self, probabilidade_a: float, probabilidade_b_dado_a: float) -> float:
        return self.probabilidade.intersecao_dependente(probabilidade_a, probabilidade_b_dado_a)
        
    def fatorial(self, n: int) -> int:
        return self.combinatoria.fatorial(n)

    def arranjo(self, total_elementos: int, qtd_escolhida: int) -> int:
        return self.combinatoria.arranjo(total_elementos, qtd_escolhida)

    def permutacao_simples(self, qtd_elementos: int) -> int:
        return self.combinatoria.permutacao_simples(qtd_elementos)

    def permutacao_repeticao(self, qtd_elementos: int, qtd_repetidas: list[int]) -> int:
        return self.combinatoria.permutacao_repeticao(qtd_elementos, qtd_repetidas)
    
    def permutacao_circular(self, qtd_elementos: int) -> int:
        return self.combinatoria.permutacao_circular(qtd_elementos)
    
    def permutacao_caotica(self, qtd_elementos: int) -> int:
        return self.combinatoria.permutacao_caotica(qtd_elementos)

    def combinacao(self, total_elementos: int, qtd_escolhida: int) -> float:
        return self.combinatoria.combinacao(total_elementos, qtd_escolhida)
    
# Subsistema 1 - calculadora de probabilidade    
class Probabilidade():
    def simples(self, casos_favoraveis: int, total_casos: int) -> float:
        return casos_favoraveis / total_casos

    def condicional(self, a_intersecao_b: float, probabilidade_a: int) -> float:
        return a_intersecao_b / probabilidade_a

    def complementar(self, probabilidade_a: float) -> float:
        return 1 - probabilidade_a
    
    def uniao(self, probabilidade_a: float, probabilidade_b: float, pa_intersecao_b: float) -> float:
        return probabilidade_a + probabilidade_b - pa_intersecao_b
    
    def intersecao_independente(self, probabilidade_a: float, probabilidade_b: float) -> float:
        return probabilidade_a * probabilidade_b
    
    def intersecao_dependente(self, probabilidade_a: float, probabilidade_b_dado_a: float) -> float:
        return probabilidade_a * probabilidade_b_dado_a

# Subsistema 2 - calculadora de combinatória    
class Combinatoria():
    def fatorial(self, n: int) -> int:
        resultado = 1

        for i in range(2, n + 1):
            resultado *= i

        return resultado

    def arranjo(self, total_elementos: int, qtd_escolhida: int) -> int:
        return (self.fatorial(total_elementos) // self.fatorial(total_elementos - qtd_escolhida))

    def permutacao_simples(self, qtd_elementos: int) -> int:
        return self.fatorial(qtd_elementos)

    def permutacao_repeticao(self, qtd_elementos: int, qtd_repetidas: list[int]) -> int:
        resultado = self.fatorial(qtd_elementos)

        for qtd in qtd_repetidas:
            resultado //= self.fatorial(qtd)

        return resultado
    
    def permutacao_circular(self, qtd_elementos: int) -> int:
        return self.fatorial(qtd_elementos - 1)
    
    def permutacao_caotica(self, qtd_elementos: int) -> int:
        if qtd_elementos == 0:
            return 1
        if qtd_elementos == 1:
            return 0

        return (qtd_elementos - 1) * (
            self.permutacao_caotica(qtd_elementos - 1)
            + self.permutacao_caotica(qtd_elementos - 2)
        )

    def combinacao(self, total_elementos: int, qtd_escolhida: int) -> int:
        return (self.fatorial(total_elementos)
                // (self.fatorial(qtd_escolhida) * self.fatorial(total_elementos - qtd_escolhida))
        )

# Implementação    
calc = CalculadoraFachada()

# Probabilidade
print(calc.probabilidade_simples(3, 10)) # 0.3
print(calc.probabilidade_condicional(0.2, 0.5)) # 0.4
print(calc.complementar(0.3)) # 0.7
print(calc.uniao(0.5, 0.4, 0.2)) # 0.7
print(calc.intersecao_independente(0.5, 0.4)) # 0.2
print(calc.intersecao_dependente(0.5, 0.3)) # 0.15

# Combinatória
print(calc.fatorial(5)) # 120
print(calc.arranjo(5, 2)) # 20
print(calc.permutacao_simples(5)) # 120
print(calc.permutacao_repeticao(6, [3, 2])) # 60 Exemplo: BANANA -> 3A, 2N
print(calc.permutacao_circular(5)) # 24
print(calc.permutacao_caotica(5)) # 44
print(calc.combinacao(5, 2)) # 10
