# git-gateway

git-gateway é uma API responsável por repassar dados de serviços de hospedagem de códigos que utilizam Git. No momento, apenas o Github é uma fonte suportada de dados. 
A aplicação é construída utilizando como linguagem Python3.7, utilizando Flask como framework para facilitar o desenvolvimento. Existe uma camada de cache atualmente que utiliza Redis e uma camada de armazenagem de dados simples utilizando MongoDB com o objetivo de simular um data lake simplificado.

## Endpoints

`GET /users/:username/repos`

Lista os repositórios públicos de um usuário no Github

`GET /repos/:username/:repo_name`

Detalha um repositório de um usuário. 

## Dependências 

### Para desenvolvimento da aplicação

- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Colocando a Aplicação de Pé

Após clonar o repositório, entre no diretório que o contém. 
Será necessário criar um arquivo `.env` com as variáveis de ambiente necessárias para rodar a aplicação. Se quiser, pode copiar o `env.sample` desse repositório para `.env`. Ele contém valores padrão para as variáveis, então na maioria dos casos é o suficiente. 

Com suas variáveis configuradas, rode: 

```shell
docker-compose up
```
Agora é só partir pro abraço! 


## Testes

Atualmente a API conta apenas com testes unitários. Foram desenvolvidos utilizando o pacote [Pytest](https://docs.pytest.org/en/stable/getting-started.html). Para rodá-los, basta estar com a aplicação funcionando e rodar:
```shell
docker exec -it git_gateway pytest
```
