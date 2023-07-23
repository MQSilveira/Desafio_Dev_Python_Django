# Sistema de Gestão de Propostas para Empréstimo Pessoal

## Estrutura do Projeto
Este projeto é composto por duas partes principais: 

### Back-end (Python)
O backend do projeto é construído utilizando o framework Django, que facilita o desenvolvimento rápido e seguro de aplicações web. Utilizamos também o Django Rest Framework para criar uma API robusta e o Django Celery em conjunto com o RabbitMQ para executar tarefas em segundo plano de forma assíncrona.

### Front-end (React)
O frontend do projeto é desenvolvido em React, uma biblioteca JavaScript de código aberto para a construção de interfaces de usuário interativas.
___

## Pré-requisitos
Certifique-se de ter os seguintes itens instalados no seu sistema:
* [Docker](https://docs.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)
___

## Orientações para executar o projeto
* Clone este repositório em seu ambiente local.
* Navegue até o "raiz" do projeto.
* Execute o comando `docker-compose up -d` para construir as imagens Docker e iniciar os contêiners do projeto.
* Após a inicialização dos contêiners, a aplicação estará rodando no endereço http://127.0.0.1:3000/ .
___

## Outros acessos
* A API estará rodando no endereço http://127.0.0.1:8000/ .
* O RabbitMQ está rodando no endereço http://localhost:15672/ .
* Você pode acessar a documentação da API no endereço http://127.0.0.1:8000/docs .
* Você pode acessar o Django Admin pelo endereço http://127.0.0.1:8000/admin/ .
> **Usuários e senhas de acesso:**<br>
> RabbitMQ= login: guest | senha: guest<br>
> Django Admin= login: admin | senha: admin
___

## Capturas de Tela Capturas de Tela
Aqui estão algumas capturas de tela da aplicação:<br>

#### Tela Principal da Aplicação:
![Formulário](https://github.com/MQSilveira/Desafio_Dev_Python_Django/blob/main/Files/pagina_formulario_em_branco.png)

#### API via "endponit" /api/v1/propostas/:
![API Propostas](https://github.com/MQSilveira/Desafio_Dev_Python_Django/blob/main/Files/enrececo_propostas.png)

#### Documentação da API:
![Documentação da API](https://github.com/MQSilveira/Desafio_Dev_Python_Django/blob/main/Files/documentacao_api.png)

#### Visualização de todas as propostas via "Django Admin":
![Visualização de todas as Propostas](https://github.com/MQSilveira/Desafio_Dev_Python_Django/blob/main/Files/admin_visualizar_todas_propostas.png)

#### Visualização de uma proposta via "Django Admin":
>**Note que não é possivel fazer qualquer tipo de alteração nos campos**

![Visualização de uma Proposta](https://github.com/MQSilveira/Desafio_Dev_Python_Django/blob/main/Files/admin_visualizar_proposta.png)

#### Cadastro de nova proposta via "Django Admin":
>**Note que não é possivel fazer inserção no campo situação**

![Inserir uma Proposta](https://github.com/MQSilveira/Desafio_Dev_Python_Django/blob/main/Files/admin_cadastro.png)
___

## Sobre o desenvolvimento do Sistema

[Neste link você encontra a documentação que contém as orientações para a criação do sistema.](https://github.com/MQSilveira/Desafio_Dev_Python_Django/blob/main/Files/README_original.md)
___

> ## Sistema de Gestão de Propostas de Empréstimo Pessoal
> Este é um desafio técnico para criar um sistema de gestão de propostas de empréstimo pessoal utilizando a seguinte stack:<br>
> * Django<br>
> * Django Rest Framework<br>
> * Django Celery<br>

**Django :** *Framework web em Python que facilita o desenvolvimento rápido e seguro de aplicações web, seguindo o padrão model-view-controller (MVC) e incluindo uma ORM para acesso ao banco de dados.*<br><br>
**Django Rest Framework:** *Biblioteca poderosa para construção de APIs em Django, fornecendo recursos avançados de serialização, autenticação, autorização e muito mais.*<br><br>
**Django Celery e RabbitMQ** *A biblioteca utiliza o Django Celery em conjunto com o RabbitMQ para executar tarefas em segundo plano (execução assíncrona), proporcionando escalabilidade e eficiência.*
___

## Tempo de Desenvolvimento
O sistema foi recebido em: 16/06/22 (sexta-feira)
Prazo estabelecido: 7 dias

Durante o período de desenvolvimento, foram realizadas as seguintes etapas:

- 16/06/22 a 18/06/22: Leitura de documentações do RabbitMQ e do Celery para compreender o funcionamento e a integração entre as tecnologias.
- 19/06/22 a 21/06/22: Construção do código do projeto, implementação das funcionalidades e testes.
- 22/06/22: Realização de pequenos ajustes e melhorias no projeto.

Foi dedicado um tempo total de 7 dias para a conclusão do sistema, incluindo o estudo das tecnologias e a construção do código.
___

## Desenvolvido por
Este projeto foi desenvolvido por: 

- **Nome do Desenvolvedor:** [Marcos Silveira](https://github.com/MQSilveira)
- **Contato:** marcosilveira.lg@gmail.com

Você também pode encontrar mais informações sobre o desenvolvedor acessando esse [LINK](https://mqsilveira.github.io/Portfolio/) ou [LinkedIn](https://www.linkedin.com/in/dev-marcos-silveira/)


