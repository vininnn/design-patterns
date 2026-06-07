## Facade

### Objetivo

O padrão Facade é um padrão estrutural que fornece uma interface simplificada para um conjunto de interfaces e subsistemas complexos.

Ele permite que o cliente interaja com apenas uma classe, sem precisar conhecer os detalhes de implementação ou a comunicação entre os subsistemas internos.

### Problema

Em alguns sistemas, funcionalidades relacionadas podem estar distribuídas em diversas classes especializadas. Embora essa divisão seja importante para a organização do código, ela pode tornar o uso da aplicação mais complexo.

O cliente passa a precisar conhecer quais classes utilizar, como instanciá-las e quais métodos chamar para realizar uma determinada operação.

À medida que o sistema cresce, essa complexidade aumenta, tornando o código mais difícil de utilizar e manter.

### Solução

O padrão Facade propõe a criação de uma classe intermediária, chamada Fachada (Facade), responsável por fornecer uma interface simples para operações mais complexas.

A fachada encapsula os detalhes dos subsistemas e coordena suas interações, permitindo que o cliente execute operações através de uma única interface. Dessa forma, o cliente não precisa conhecer a estrutura interna do sistema.

### Estrutura

O padrão é composto por três elementos principais:

* **Client**: código que utiliza a fachada.
* **Facade**: classe responsável por simplificar o acesso aos subsistemas.
* **Subsystems**: conjunto de classes responsáveis pela implementação das funcionalidades do sistema.

### Exemplo Implementado

Código: [facade.py](facade.py)

Neste projeto foi implementada uma calculadora de Probabilidade e Combinatória.

As operações foram divididas em dois subsistemas:

* `Probabilidade`
* `Combinatoria`

A classe `Probabilidade` é responsável pelos cálculos relacionados à teoria das probabilidades, como probabilidade simples, condicional, complementar, união e interseção de eventos.

A classe `Combinatoria` é responsável pelos cálculos de análise combinatória, como fatorial, arranjo, combinação e diferentes tipos de permutação.

A classe `CalculadoraFachada` atua como a **Facade**, oferecendo uma única interface para acessar as funcionalidades dos dois subsistemas.

Dessa forma, o cliente não precisa instanciar ou interagir diretamente com as classes `Probabilidade` e `Combinatoria`, utilizando apenas a fachada para realizar os cálculos necessários.

### Benefícios

* Simplifica o uso de sistemas complexos.
* Reduz o acoplamento entre cliente e subsistemas.
* Centraliza o acesso às funcionalidades do sistema.
* Facilita a manutenção e evolução do código.
* Oculta detalhes de implementação dos subsistemas.

### Referência

Refactoring Guru — Facade Pattern:
https://refactoring.guru/design-patterns/facade
