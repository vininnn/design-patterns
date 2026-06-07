## Factory Method

### Objetivo

O padrão Factory Method é um padrão criacional que define uma interface para criação de objetos, permitindo que subclasses decidam qual classe concreta será instanciada.

Dessa forma, o código cliente trabalha com abstrações, sem depender diretamente das classes concretas que estão sendo criadas.

### Problema

Em muitos sistemas, o código responsável pela lógica de negócio também precisa criar objetos específicos para executar determinadas tarefas.

Quando essas classes concretas são instanciadas diretamente, o código fica fortemente acoplado às implementações utilizadas. Isso dificulta a manutenção e a extensão do sistema, pois qualquer alteração nos tipos de objetos criados pode exigir modificações em várias partes do código.

### Solução

O padrão Factory Method propõe delegar a criação dos objetos para um método específico, chamado Factory Method.

A classe base (Creator) declara esse método e implementa a lógica de negócio utilizando apenas a abstração do produto. As subclasses (Concrete Creators) sobrescrevem o Factory Method para decidir qual produto concreto será criado.

Dessa forma, novas implementações podem ser adicionadas sem alterar a lógica existente.

### Estrutura

O padrão é composto por quatro elementos principais:

* **Product**: interface ou classe abstrata que define os produtos criados.
* **Concrete Products**: implementações concretas do produto.
* **Creator**: classe abstrata que declara o Factory Method e contém a lógica de negócio.
* **Concrete Creators**: subclasses responsáveis por criar produtos concretos específicos.

### Exemplo Implementado

Código: [factory-method.py](factory-method.py)

Neste projeto foi implementado um sistema de processamento de pagamentos.

A classe abstrata `Pagamento` representa o **Product**, definindo a operação comum para todos os tipos de pagamento.

As classes `PagamentoPix`, `PagamentoCartao` e `PagamentoBoleto` representam os **Concrete Products**, implementando a forma específica de realizar cada pagamento.

A classe abstrata `ProcessadorPagamento` atua como o **Creator**. Ela define o método `criar_pagamento()`, responsável pela criação do produto, e contém a lógica de negócio no método `processar_pagamento()`.

As classes `ProcessadorPix`, `ProcessadorCartao` e `ProcessadorBoleto` representam os **Concrete Creators**. Cada uma sobrescreve o Factory Method para retornar um tipo específico de pagamento.

Quando o processamento é iniciado, a lógica definida no Creator utiliza o Factory Method para obter o produto adequado sem conhecer sua implementação concreta.

### Benefícios

* Reduz o acoplamento entre cliente e produtos concretos.
* Facilita a adição de novos tipos de produtos.
* Centraliza a lógica de criação dos objetos.
* Favorece a aplicação do princípio Aberto/Fechado (Open/Closed Principle).
* Permite que a lógica de negócio trabalhe apenas com abstrações.

### Referência

Refactoring Guru — Factory Method Pattern:
https://refactoring.guru/design-patterns/factory-method
