# Docker com Python, Flask e MySQL

Este projeto cria um ambiente de desenvolvimento utilizando o docker para aplicações que necessitam de python, flask e mysql.

Para alterar, basta atualizar o Dockerfile ou docker-compose.

Para adicionar depências, pode ser adicionado no arquivo requirements.txt, que é utilizado pelo Dockerfile para instalar através do pip.

## Modo de utilização

Para iniciar os containers, basta rodar o comando:

```
$ docker-compose up - d
```

Para parar os containers, basta:
```
$ docker-compose down
```