# API-Django

Foi proposto um desafio técnico, para a criação de uma API em Django, no qual é necessário que seja possível o cadastro de novos usuários e grupos de usuários
na aplicação, além de poder editar e excluir os cadastros.

## Requisitos
* [Python 3](https://www.python.org/downloads/)
* [Banco de dados PostgreSQL](https://www.postgresql.org/download/)

## Descrição

Para conseguir executar a aplicação serão necessários alguns passos:
- Clonar o repositório em sua máquina;
- Acessar o arquivo setting.py, localizado na pasta ApiDesafio e configurar o seu banco de dados, caso não tenha o PostgreSQL, é só descomentar o SQLite e comentar o PostgreSQL;
- Abrir o terminal e executar o comando **"python manage.py migrate"**, para realizar a migração das tabelas, para o seu banco de dados;
- Abrir o terminal e executar o comando **"python manage.py runserver"**, com isso, a aplicação irá iniciar no endereço: http://127.0.0.1:8000/, caso a porta não esteja em uso;
- Por último é só inserir o caminho **/api/v1/**, que irá acessar a raiz da api;
- A api é composta por duas rotas **/api/v1/grupos/** e **/api/v1/usuarios/** e contem os métodos GET, POST, PUT e DELETE. 
## Autor
* [Weslley Gomes](https://www.linkedin.com/in/weslley-joaquim-gomes/)
