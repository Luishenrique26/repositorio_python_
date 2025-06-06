<a href= 'https://www.python.org/'>
    <img src='https://skillicons.dev/icons?i=python'/>
    <img src='https://cdn.discordapp.com/attachments/1273399725479039101/1377437755931361340/images.png?ex=684036a0&is=683ee520&hm=1c1571ddd3d9c31f921f0f0fb23444a6e41e64f5b8a9e1ed9694f7d434446bc7&'/>
  
    
</a>

## 🔹 Integrantes do Grupo

- Gabriel Souza (Matrícula: 202408151391)
- Luis Henrique (Matrícula: 202403317788)
- Lucas Thomaz (Matrícula: 202403317753)
- Emerson Nascimento (Matrícula: 202403317771)

# 🔹 Nome da Aplicação
Sistema de gerenciamento de atividades de projetos sociais

  <img src='https://cdn.discordapp.com/attachments/1273399725479039101/1377443880231764028/BCO.png?ex=68403c54&is=683eead4&hm=0212fb17c84a1072526576aedd2a91859b8ad9767af8c03bdf30d53c71dcf1ba&'/>
  

## Descrição

Esta aplicação tem como objetivo, gerenciar atividade por meio de um sistema de cadastro. Ela permite que os usuários, criem atividades e possa modificá-las e excluí-las sempre que quiserem. 

## Funcionalidades Principais

Cadastro e login de usuários

Criação, edição,descrição das atividades e exclusão de atividades

Registro de data para cada atividade

Listagem de todas as atividades criadas

## 🧰 Requisitos

Certifique-se de que você tem o Python instalado, utilizando o Tkinter como interface gráfica, desenvolver e implementar funcionalidades. Criar, Editar, e Excluir na aplicação, aproveitando o poder do SQL. A aplicação utiliza apenas bibliotecas padrão, então não há necessidade de instalar pacotes externos.


## ✅ Dependências

- Python 3.8 ou superior
- Tkinter
- Pydantic
- Bcrypt

## 🗂️ Estrutura do Projeto
```sh
├── database/

│   ├── migrations/

│   │   ├── sql/

│   │   │   ├── 01_create_table_user.sql

│   │   │   ├── 02_create_table_activities.sql

│   │   │   ├── __init__.py

│   │   │   ├── migrations.py

│   │   ├── config.py

├── src/

│   ├── common/

│   │   ├── base.py

│   │   ├── utils.py  

│   ├── domain/

│   │   ├── dtos/

│   │   │   ├── __init__.py

│   │   │   ├── activities_dto.py

│   │   │   ├── login_dto.py

│   │   │   ├── user_dto.py

│   ├── entities/

│   │   ├── __init__.py

│   │   ├── activities_entity.py

│   │   ├── user_entity.py

│   │   ├── __init__.py

│   ├── front/

│   │   ├── activities/

│   │   │   ├── init.py

│   │   │   ├── add_activities.py

│   │   │   ├── list_activities.py

│   │   │   ├── update_activities.py

│   │   ├── __init__.py

│   │   ├── login.py

│   │   ├── register.py

│   │   ├── report.py

│   ├── repositories/

│   │   ├── __init__.py

│   │   ├── activities_repository.py

│   │   ├── user_repository.py

│   ├── services/

│   │   │   ├── __init__.py

│   │   │   ├── activities_service.py

│   │   │   ├── auth_service.py

│   │   │   ├── user_service.py

├── __init__.py

├── .gitignore

├── database.db

├── main.py

├── README.md

├── relatorio.log

├── requirements.txt
```


##  💻 Comando para instalar o requiriments.txt em sua máquina

- pip install -r requirements.txt



  






