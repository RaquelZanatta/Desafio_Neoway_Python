# Docker - Python - PostgreSQL

Este é um serviço de ETL desenvolvido na linguagem Python que realiza as seguintes etapas:

- lê um arquivo csv em formato tabular;
- transforma os dados em um DataFrame utilizando a biblioteca Pandas;
- valida se todos os CPFs e CNPJs estão válidos, armazenando as informações em 3 novas colunas inseridas no DataFrame;
- realiza a conexão com o banco de dados Postgree utilizando a bilbioteca sqlalchemy;
- cria a tabela e insere os dados no banco de dados.

Para a execução do serviço, foram criados os arquivos DockFile e docker-compose, responsáveis por criar os conteiners necessários para executar a aplicação. Sendo eles:

- Python: responsável pela execução da lógica do serviço;
- Postgree: responsável por hospedar o banco de dados que armazena os dados;
- Adminer: responsável por hospedar a aplicação Adminer, utilizada para acessar e visualizar o banco de dados.


Para executar a aplicação, siga os passos abaixo:

- Abra um terminal na pasta raiz do projeto e execute o comando:

  - docker-compose up -d
- Após o término do processo acima, execute o seguinte comando para rodar o serviço:

  - docker-compose run app
- Abra um navegador e acesse a URL http://localhost:8081/ com os seguintes dados:

  - Sistema: PostgreSQL
  - Servidor: db
  - Usuário: neoway2023
  - Senha: neoway2023
  - Base de dados: clients
