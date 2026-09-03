## Sobre o projeto

O Jogo da Vida é um autômato celular criado pelo matemático **John Conway** em 1970. O sistema simula a evolução de uma população de células em uma grade bidimensional, na qual cada célula pode estar viva ou morta.

A evolução da população ocorre automaticamente a cada geração, sendo determinada exclusivamente pela configuração da geração anterior.

Neste projeto, a simulação é realizada em um **tabuleiro 10×10**, utilizando os símbolos `O` para representar células vivas e `.` para representar células mortas.

## Funcionamento

Ao iniciar o programa, o usuário pode escolher entre:

* **Matriz aleatória:** o programa gera automaticamente uma configuração inicial;
* **Matriz personalizada:** o usuário escolhe quais células do tabuleiro estarão vivas.

A matriz personalizada permite informar a posição das células vivas através de suas linhas e colunas. O programa também verifica se as posições informadas são válidas e impede que uma mesma célula seja adicionada mais de uma vez.

## Regras do Jogo da Vida

Cada célula considera as **8 posições vizinhas** — incluindo as diagonais — para determinar seu estado na próxima geração.

As regras implementadas são:

| Situação                                     | Resultado                |
| -------------------------------------------- | ------------------------ |
| Célula viva com menos de 2 vizinhos vivos    | Morre por solidão        |
| Célula viva com 2 ou 3 vizinhos vivos        | Sobrevive                |
| Célula viva com mais de 3 vizinhos vivos     | Morre por superpopulação |
| Célula morta com exatamente 3 vizinhos vivos | Torna-se viva            |

Essas regras são aplicadas a todas as células a cada nova geração.

## Visualização

A matriz é exibida diretamente no terminal. A cada nova geração, o terminal é limpo e o novo estado do tabuleiro é apresentado, juntamente com o número da geração atual.
Há também um intervalo de **1 segundo entre as gerações**, permitindo acompanhar visualmente a evolução da população.

## Detecção de padrões repetitivos

Além das regras básicas do problema, o programa mantém um **histórico das gerações anteriores**.

Cada nova geração é comparada com as configurações armazenadas. Quando uma matriz volta a ser igual a uma configuração anterior, o programa identifica que a população entrou em um padrão repetitivo e encerra a simulação, exibindo a geração em que isso foi detectado.

## Modularização

O programa foi estruturado utilizando funções para separar as diferentes responsabilidades do sistema:

* `matriz_aleatoria()` — gera a configuração inicial aleatória;
* `exibir_matriz()` — exibe a matriz no terminal;
* `matriz_personalizada()` — permite ao usuário definir a configuração inicial;
* `contar_vizinhos()` — contabiliza as células vivas vizinhas;
* `matrizes_iguais()` — compara duas configurações;
* `matriz_copia()` — cria uma cópia da matriz para o histórico;
* `proxima_geracao()` — calcula a próxima geração;
* `jogo_da_vida()` — controla a execução principal da simulação.

A modularização era uma das exigências do problema e foi utilizada para organizar as principais tarefas do software.

## Tecnologias

* **Python**
* `random` — geração de matrizes aleatórias;
* `os` — limpeza do terminal;
* `time` — controle do intervalo entre gerações.

As bibliotecas utilizadas são importadas no início do programa.

## Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd NOME_DO_REPOSITORIO
```

Execute o programa:

```bash
python3 AntonioCarneiro.py
```

O programa será iniciado no terminal e solicitará a escolha da configuração inicial.

## Contexto acadêmico

**Instituição:** Universidade Estadual de Feira de Santana — UEFS
**Curso:** Engenharia de Computação
**Disciplina:** EXA855 - MI Algoritmos
**Problema:** 2
**Tema:** O Jogo da Vida
**Período:** 2025.1
**Linguagem:** Python

O problema foi iniciado em **09/04/2025**, com entrega do código prevista para **02/05/2025** e do relatório para **04/05/2025**.

## Autoria

Projeto desenvolvido individualmente como atividade acadêmica da MI Algoritmos.

O código contém a declaração de autoria e não plágio exigida pela atividade.
