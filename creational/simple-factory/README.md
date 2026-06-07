## Simple Factory

> **Observação:** A Simple Factory não é um dos 23 padrões clássicos catalogados pelo GoF (Gang of Four). Apesar disso, é uma técnica amplamente utilizada para encapsular a criação de objetos e costuma ser apresentada como uma etapa intermediária ao Factory Method ou Abstract Factory.

### Objetivo

A Simple Factory centraliza a criação de objetos em uma única classe responsável por decidir qual implementação concreta deve ser instanciada.

Seu objetivo é reduzir o acoplamento entre o código cliente e as classes concretas, evitando que o cliente precise conhecer diretamente os detalhes de criação dos objetos.

### Problema

Em muitos sistemas, diferentes objetos podem ser utilizados para realizar a mesma tarefa. Uma implementação comum consiste em criar esses objetos diretamente no código cliente utilizando diversas estruturas condicionais.

Exemplo:

```python
if tipo == "pix":
    pagamento = PagamentoPix()
elif tipo == "cartao":
    pagamento = PagamentoCartao()
elif tipo == "boleto":
    pagamento = PagamentoBoleto()
```

Entretanto, à medida que novos tipos são adicionados, essas estruturas condicionais tendem a crescer e se espalhar pelo sistema, aumentando o acoplamento e dificultando a manutenção.

### Solução

A Simple Factory propõe concentrar a lógica de criação em uma classe específica.

Em vez de instanciar diretamente os objetos concretos, o cliente solicita à fábrica que crie o objeto desejado.

Dessa forma, a lógica de criação fica centrada à um único local e o código cliente passa a depender apenas da abstração do produto.

### Estrutura

A implementação é composta por três elementos principais:

* **Factory**: responsável por decidir qual produto concreto será criado.
* **Product**: interface ou classe abstrata que define as operações comuns aos produtos.
* **Concrete Products**: implementações concretas do produto.

### Exemplo Implementado

Código: [simple-factory.py](simple-factory.py)

Neste projeto foi implementado um sistema de pagamentos.

A classe abstrata `Pagamento` representa o **Product**, definindo a operação comum para todos os meios de pagamento.

As classes `PagamentoPix`, `PagamentoCartao` e `PagamentoBoleto` representam os **Concrete Products**, implementando a forma específica de realizar cada pagamento.

A classe `FabricaPagamentos` representa a **Factory**, sendo responsável por decidir qual objeto concreto deve ser criado com base no tipo de pagamento informado.

O cliente solicita a criação do objeto à fábrica e utiliza o produto retornado sem precisar conhecer os detalhes de sua implementação.

### Estrutura da Implementação

```
Cliente
    |
    v
FabricaPagamentos
    |
    +--> PagamentoPix
    +--> PagamentoCartao
    +--> PagamentoBoleto
```

### Diferença para Factory Method

A principal diferença entre a Simple Factory e o Factory Method está na forma como a criação dos objetos é organizada.

Na **Simple Factory** existe uma única fábrica responsável por decidir qual objeto será criado:

```
Cliente
    |
    v
FabricaPagamentos
    |
    +--> PagamentoPix
    +--> PagamentoCartao
    +--> PagamentoBoleto
```

Já no **Factory Method** a responsabilidade de criação é distribuída entre diferentes criadores concretos:

```
                Cliente
                    |
                    v
    ProcessadorPagamento(Creator)
                    ^
                    |               
    +---------------+---------------+
    |               |               |
    |               |               |
ProcessadorPix ProcessadorCartao ProcessadorBoleto


            Pagamento(Product)
                    ^ 
                    |   
    +---------------+---------------+
    |               |               |
    |               |               |
PagamentoPix PagamentoCartao PagamentoBoleto
```

Enquanto a Simple Factory utiliza uma única classe para decidir qual produto criar, o Factory Method utiliza herança para permitir que subclasses definam qual produto concreto será instanciado.

Por esse motivo, a Simple Factory costuma ser considerada uma solução mais simples e direta, enquanto o Factory Method oferece maior flexibilidade e extensibilidade.

### Benefícios

* Centraliza a criação dos objetos.
* Reduz o acoplamento entre cliente e implementações concretas.
* Facilita a manutenção do código.
* Evita repetição de lógica de criação.

### Limitações

* A fábrica tende a crescer conforme novos produtos são adicionados.
* Geralmente exige modificações na fábrica sempre que um novo produto é criado.
* Possui menor flexibilidade que o Factory Method.

### Referências

Refactoring Guru — Factory Comparison:
https://refactoring.guru/design-patterns/factory-comparison

Refactoring Guru — Factory Method Pattern:
https://refactoring.guru/design-patterns/factory-method