## State

### Objetivo

O padrão State é um padrão comportamental que permite que um objeto altere seu comportamento quando seu estado interno muda. Na prática, o objeto parece mudar de classe conforme o estado atual.

### Problema

Em muitos sistemas, um objeto pode assumir diferentes estados ao longo de sua execução. Uma implementação comum consiste em utilizar diversas estruturas condicionais (`if`,`switch`/`match`) para verificar o estado atual e decidir qual comportamento executar.

À medida que novos estados e regras de transição são adicionados, essas estruturas condicionais tendem a crescer, tornando o código difícil de manter e expandir.

### Solução

O padrão State propõe encapsular cada estado em uma classe específica. Em vez de concentrar toda a lógica em uma única classe utilizando condicionais, o objeto principal (Context) delega o comportamento para um objeto que representa o estado atual.

Quando ocorre uma transição, o contexto substitui o estado atual por outro objeto de estado. Dessa forma, cada estado é responsável apenas pelo comportamento relacionado a ele.

### Estrutura

O padrão é composto por três elementos principais:

* **Context**: objeto principal que possui um estado atual.
* **State**: interface ou classe abstrata que define as operações comuns aos estados.
* **Concrete States**: implementações concretas dos estados possíveis.

### Exemplo Implementado
Código: [state.py](state.py)

Neste projeto foi implementado um sistema de semáforo.

O semáforo pode assumir três estados:

* Vermelho
* Verde
* Amarelo

A classe `Semaforo` atua como o **Context**, armazenando uma referência para o estado atual.

A classe abstrata `Estado`, assim como o nome diz, é o **State**, ele define a interface comum para todos os estados.

As classes `Vermelho`, `Amarelo` e `Verde` representam os **Concrete States**. Cada uma implementa a lógica de transição para o próximo estado.

Quando o método de mudança de estado é executado, o comportamento é delegado ao estado atual. Esse estado decide qual será o próximo estado do semáforo e solicita a atualização do contexto.

### Benefícios

* Elimina grandes estruturas condicionais.
* Facilita a adição de novos estados.
* Separa responsabilidades em classes menores.
* Torna o código mais organizado e extensível.

### Referência

Refactoring Guru — State Pattern:
https://refactoring.guru/design-patterns/state
