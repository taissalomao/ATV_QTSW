# Projeto de Exercícios com Testes

Bem-vindo ao projeto de exercícios com testes! Este repositório contém várias tarefas e testes para demonstrar técnicas de desenvolvimento de software, como o desenvolvimento orientado por testes (TDD).

## Estrutura do projeto

- **`exercicio_um`**: Pasta contendo o código e testes do Exercício Triângulo.
- **`exercicio_dois`**: Pasta contendo o código e testes do Exercício Person / Email.
- **`exercicio_tres`**: Pasta contendo o código e testes do Exercício Calculadora.
- **`requirements.txt`**: Arquivo contendo as dependências necessárias para executar os testes.
- **`README.md`**: Este arquivo, com instruções sobre como executar os testes e informações sobre o projeto.

## Configuração do ambiente

Antes de começar, certifique-se de que tenha feito o clone desse repositório.


1. **Crie um ambiente virtual**:

    No terminal, execute o seguinte comando na raiz do projeto para criar um ambiente virtual chamado `venv`:

    ```shell
    python -m venv venv
    ```

2. **Ative o ambiente virtual**:

    - No Windows:

        ```shell
        venv\Scripts\activate
        ```

    - No macOS/Linux:

        ```shell
        source venv/bin/activate
        ```

## Instalação de dependências

Com o ambiente virtual ativo, instale as dependências necessárias para executar os testes:

```shell
pip install -r requirements.txt
```

## Execução dos testes

Para executar os testes, você precisará entrar em cada diretório de exercício e executar o arquivo de testes correspondente.

Por exemplo, para o Exercício 1:

1. Navegue até o diretório exercicio_um:

    ```shell
    cd exercicio_um
    ```

2. Execute o arquivo de testes usando o `pytest`:

    ```shell
    pytest teste_triangulo.py
    ```

Repita o processo para cada exercício, substituindo `exercicio_um` pelo diretório do exercício desejado e o nome do arquivo de testes conforme apropriado (`test_exercicio_dois.py`, `test_exercicio_tres.py`).

Certifique-se de estar dentro do ambiente virtual com as dependências instaladas antes de executar os testes.
