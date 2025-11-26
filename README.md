# Projeto2_FCCPD

<details>
  <summary>Guia desafio 1</summary>

  Esse desafio consiste na criaçã de dois contêiner que se comunicam através de uma rede Docker
  - Servidor Web (Flask) na porta 8080
  - Client (Requisições periódicas)

  Cria a rede:
  ``` docker network create redeD1```
  Build da imagem do Servior:
  ```docker build -t servidord1 ./desafio1/servidor```
  Build da imagem do Cliente:
  ```docker build -t cliented1 ./desafio1/cliente```
  Subir o servidor:
  ```docker run -d --name server --network redeD1 -p 8080:8080 servidord1```
  Subir o cliente:
  ```docker run -d --name cliented1 --network redeD1 cliented1```
  Visualizar os logs do cliente:
  ```docker logs -f cliented1```
</details>
