# Introdução

Tecnologias:

- Python, como linguagem de programação;

- Django Framework, como framework de desenvolvimento web para o backend;

- Django Rest Framework, como biblioteca para o Django Framework para criação de APIs Restful;

- SQLite, como SGBD para armazenar, acessar, atualizar e deletar informações no banco de dados;

# Configurações

### Migrations

- Agora deve-se rodar as migrações para o banco ser preenchido com as tabelas necessárias à aplicação:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Admin

- Após estas configurações iniciais, o projeto já estará pronto para uso, logo, deve-se criar um super user para o acesso do Django Admin:

```bash
python manage.py createsuperuser
```

# Problema

- Criei 2 Django Apps, a primeira é a 'backendGraoDireto', com as configuraçoes do Django Framework, e a segunda é a 'api', com as informações de user e restaurants;
- Herdei o model User do Django Framework para a criação de novos usuários, e utilizei uma flag booleana para indicar se é admin;
- Sobre criptografia dos dados: https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#how-django-stores-passwords

# Rotas

### Autenticação

- Login

```bash
url: localhost:8000/api/login
method: POST
body: "email", "password"
```

- Logout

```bash
url: localhost:8000/api/logout
method: POST
```

> As próximas rotas só poderão ser acessadas com o Login feito

### Rotas

- Restaurants List

```bash
url: localhost:8000/api/restaurants/
method: GET
```

- Resturant Details

```bash
url: localhost:8000/api/details/:id/
method: GET
```
