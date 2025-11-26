# Projeto2_FCCPD

<details>
  <summary><strong>Guia desafio 1 - Contêiner em Rede</strong></summary><br>
  
  Esse desafio consiste na criação de dois contêineres que se comunicam através de uma rede Docker:
  - Servidor Web (Flask) na porta 8080
  - Client (Requisições periódicas)

  Passo a passo de como rodar o desafio:<br>
  1. Cria a rede:
  ```docker network create redeD1```<br>
  2. Build da imagem do Servior:
  ```docker build -t servidord1 ./desafio1/servidor```<br>
  3. Build da imagem do Cliente:
  ```docker build -t cliented1 ./desafio1/cliente```<br>
  4. Subir o servidor:
  ```docker run -d --name server --network redeD1 -p 8080:8080 servidord1```<br>
  5. Subir o cliente:
  ```docker run -d --name cliented1 --network redeD1 cliented1```<br>
  6. Visualizar os logs do cliente:
  ```docker logs -f cliented1```
</details>

<details>
  <summary><strong>Guia desafio 2 - Volume e Persistência</strong></summary>
  Nesse desafio foi implementado um contêiner (PostgreSQL) com persistência de dados usando volume
  <br><br>

  Passo a passo de como rodar o desafio:<br>
  1. Subir o banco PostgreSQL:
  ```docker compose up -d```<br>
  2. Acessa o banco de dados:
  ```docker exec -it desafio2 psql -U admin -d teste```<br>
  3. Cria a tabela e insere os dados:
  ```
  CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome TEXT
  );
    
  INSERT INTO alunos (nome) VALUES ('Thiago');
  INSERT INTO alunos (nome) VALUES ('Maria');
    
  SELECT * FROM alunos;
  ```
  
  4. Sair do PostgreSQL:
  ````\q````<br>
  5. Derruba o contêiner:
  ```docker compose down```

  6. Para testar a persistência do dado faça:
  ````docker compose up -d````
  ````docker exec -it desafio2 psql -U admin -d teste````
  ````SELECT * FROM alunos;````
</details>
