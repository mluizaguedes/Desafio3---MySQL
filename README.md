## DevWeb
Repositório criado para a aula de Programação em Microinformática - 1SEM;

### Projeto Flask com MySQL.
Criado uma aplicação web simples para uma empresa fictícia, este projeto utiliza HTML, CSS, flask e MySQL.

### Pré-requisitos

- Python 3.x instalado
- MySQL configurado e em execução
- Biblioteca `Flask` e dependências listadas no arquivo `requirements.txt`

### Configuração

1. **Execute o MySQL e carregue os códigos do arquivo `database.sql`:**  
Certifique-se de que o MySQL está em execução e use o conteúdo do arquivo `database.sql` para configurar o banco de dados.  

2. **Edite o arquivo app.py:**
Atualize o arquivo app.py com a senha do seu MySQL:

```bash 
    app.config['MYSQL_PASSWORD'] = 'SUA SENHA AQUI'
```

3. **Crie e ative um ambiente virtual:**
No terminal do VSCode, execute os seguintes comandos:

```bash
python -m venv venv
venv\Scripts\activate
```

4. **Instale as dependências:**
Instale o Flask e outras bibliotecas necessárias:

```bash
pip install flask
pip install flask_mysqldb
```

5. 
```bash
pip freeze > requirements.txt
```

6. **Inicie a aplicação Flask:**
Execute o servidor de desenvolvimento com o comando:

```bash
flask run --debug
```

#### Observações
- O arquivo `database.sql` deve conter as instruções SQL necessárias para criar e popular o banco de dados.
- Certifique-se de que as configurações no `app.py` estão corretas, incluindo o nome do banco de dados, usuário e senha.