## Executar o projeto

De forma a poder executar o projeto, é aconselhado que o utilizador tenha instalado na sua máquina o docker-compose. Mais informação sobre a sua instalação pode ser encontrada [aqui](https://docs.docker.com/compose/install/).

Logo de seguida, o utilizador deve navegar até à diretoria `app` e executar o seguinte comando:

```sh
    docker-compose up --build
```

Este comando vai fazer build e executar todos os containers necessários para o projeto.

Caso o comando acima seja bem sucedido, o projeto está pronto a ser utilizado. Assim, o utilizador poderá, noutro terminal, executar o novo comando:

```sh
    docker-compose exec scheduler python manage.py createsuperuser
```

Este comando serve para criar um super utilizador de sistema.

## Executar os testes unitários

De forma a executar os testes unitários, o projeto deve estar up. E num novo terminal deve ser executado o comando:

```sh
    docker-compose exec scheduler python manage.py test
```
