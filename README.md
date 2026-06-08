# RPG EDUCACIONAL API 🚀

Este projeto consiste em uma API REST desenvolvida em **Python** utilizando **Django** e **Django REST Framework (DRF)**. O foco central é a aplicação prática de **Polimorfismo, Inversão de Dependência e Arquitetura em Camadas**, utilizando interfaces baseadas em Classes Abstratas para simular contratos e injeção dinâmica de implementações.

## 📚 Objetivo

Demonstrar a aplicação de padrões de projeto e princípios de POO em um framework (Django),
garantindo:

* **Desacoplamento:** Camadas de Controller e DAO isoladas.
* **Polimorfismo:** Troca dinâmica de implementações via `config.py`.
* **Contratos:** Uso de classes base para definir comportamentos obrigatórios.

## 🧠 Estratégia Polimórfica

O projeto organiza a lógica de persistência e controle em três partes:

### 1. Controllers

Baseados em interfaces (`api/interfaces/controllers/`), definem métodos CRUD (`salvar`, `alterar`, `deletar`, `consultar`, `consultarbyId`).

* **Exemplo:** `ContaControllerImpl` implementa a lógica, delegando a persistência ao DAO injetado.

### 2. DAO (Data Access Object)

Baseados em interfaces (`api/interfaces/daos/`), abstraem a comunicação com o banco de dados.

* **Implementação:** `NomeEntidadeDAO_Mysql` realiza a persistência via **Django ORM** e **MySQL**.

### 3. Injeção de Dependência via `config.py`

O arquivo `api/config.py` atua como o orquestrador. Ele define quais classes concretas serão instanciadas em tempo de execução:

```python
# Exemplo de configuração de injeção
CONFIG = {
    'IContaDAO': 'api.persistence.ContaDAO_Mysql.ContaDAOMysql',
    'IContaController': 'api.controllers.ContaController.ContaControllerImpl',
}

```

Isso permite alterar o comportamento da aplicação (trocar o DAO de MySQL para outro, por exemplo) sem alterar o código do Controller ou da View.

## ⚙️ Tecnologias Utilizadas

* **Python 3.14**
* **Django 6.0.6**
* **Django REST Framework**
* **MySQL** (Banco de dados local via MySQL Workbench)
* **drf-spectacular** (Swagger/OpenAPI)

## 🏗️ Fluxo da Aplicação

1. A **View** recebe a requisição HTTP.
2. A View chama a função `inject()` de `config.py`.
3. O `config.py` instancia dinamicamente o **Controller** e seu respectivo **DAO**.
4. O Controller processa a regra de negócio e retorna um dicionário padrão para a View, que responde com um `JsonResponse`.

## 🛠️ Execução

```bash
# 1. Clone o repositório
git clone <seu-link-github>
cd <nome-do-projeto>

# 2. Ative o ambiente virtual
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o banco local (MySQL Workbench)
# Crie o banco: CREATE DATABASE rpg_educacional_db;

# 5. Aplique as migrações e rode o servidor
python manage.py migrate
python manage.py runserver

```

**Servidor:** `http://localhost:8000/api/`
**Documentação (Swagger):** `http://localhost:8000/api/docs/`

## 🎯 Conclusão

O projeto prova que, mesmo utilizando frameworks opinativos como o Django, é possível aplicar conceitos avançados de engenharia de software para garantir um código modular, extensível e testável, separando a lógica de negócio da infraestrutura de persistência.

## 👨‍💻 Grupo

* Arthur Daniel Ribeiro Pereira Dantas Lourenço
* Danilo Moraes Borges Piquiá
* Matheus Oliveira Gouveia Campos

---

*Nota: Este projeto utiliza um banco de dados MySQL rodando localmente (localhost:3306).*