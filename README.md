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
  1. Entra no diretório: ````cd desafio2````<br>
  2. Subir o banco PostgreSQL:
  ```docker compose up -d --build```<br>
  3. Acessa o banco de dados:
  ```docker exec -it desafio2 psql -U admin -d teste```<br>
  4. Cria a tabela e insere os dados:
  ```
  CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome TEXT
  );
    
  INSERT INTO alunos (nome) VALUES ('Thiago');
  INSERT INTO alunos (nome) VALUES ('Maria');
    
  SELECT * FROM alunos;
  ```
  
  5. Sair do PostgreSQL:
  ````\q````<br>
  6. Derruba o contêiner:
  ```docker compose down```

  7. Para testar a persistência do dado faça:
  ````docker compose up -d````
  ````docker exec -it desafio2 psql -U admin -d teste````
  ````SELECT * FROM alunos;````
</details>

<details>
  <summary><strong>Guia desafio 3 - Docker Compose Orquestrando Serviços</strong></summary>
  
  Nesse desafio usa-se Docker compose para orquestrar múltplos serviços dependentes:
  - Servidor Web;
  - Banco de Dados;
  - Cache

  Passo a passo de como rodar o desafio:<br>
  1. Subir os Contêineres:
  ```docker compose up -d --build```<br>
  2. Testar Servidor Web:
  ```curl http://localhost:8000```<br>
  3. Validar Conexão com Redis (Cache)
  ```curl http://localhost:8000/cache-test```
  4. Testar Banco de Dados (PostgreSQL):
  ```curl http://localhost:8000/db-data```<br>
  5. Verificar persistência dos dados:
  ```curl http://localhost:8000/db-data```
</details>

<details>
  <summary><strong>Guia desafio 4 - Microsserviços Independentes</strong></summary>
  
  Nesse desafio foi criado dois microsserviços independentes que se comunicam através de HTTP
  - Microsserviço 1 (Lista de Usuários Json)
  - Microsserviço 2 (Consome o serviço 1)

  Passo a passo de como rodar o desafio:<br>
  1. Subir os contêineres dos microsserviços:
  ```docker compose up -d --build```<br>
  2. Testar Microsserviço 1:
  ```curl http://localhost:5001/usuarios```<br>
  3. Testar Microsserviço 2:
  ```curl http://localhost:5002/info-usuarios```
</details>

<details>
  <summary><strong>Guia desafio 5 - Microsserviços com API Gateway</strong></summary>

  Nesse desafio foi criado uma arquitetura com API Gateway que centraliza o acesso aos dois microsserviços
  - Microsserviço 1 (Fornece dados dos usuários)
  - Microsserviço 2 (Fornece os pedidos)
  - Gateway (Usa endpoints: /usuarios e /pedidos)

  Passo a passo de como rodar o desafio:<br>
  1. Subir os contêineres:
  ```docker compose up -d --build```<br>
  2. Testar Gateway - endpoint de usuários:
  ```curl http://localhost:8000/usuarios```<br>
  3. Testar Gateway - endpoint de pedidos:
  ```curl http://localhost:8000/pedidos```
</details>
