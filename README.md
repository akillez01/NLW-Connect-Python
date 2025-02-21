# NLW Connect Python

Este é um projeto desenvolvido durante o evento NLW Connect, utilizando Python e Flask para criar uma API para gerenciamento de eventos e inscrições.

## Estrutura do Projeto

- **src/main/routes**: Contém as rotas da API.
  - `event.py`: Rotas relacionadas a eventos.
  - `subs.py`: Rotas relacionadas a inscrições.
  - `events_link.py`: Rotas relacionadas a links de eventos.

- **src/controllers**: Contém os controladores que gerenciam a lógica de negócios.
  - `events/events_creator.py`: Lógica para criação de eventos.
  - `subscribers/subscribers_creator.py`: Lógica para criação de inscrições.
  - `subscribers/subscribers_manager.py`: Lógica para gerenciamento de inscrições.
  - `events_link/events_link_creator.py`: Lógica para criação de links de eventos.

- **src/model**: Contém a camada de dados.
  - `configs`: Configurações do banco de dados.
  - `entities`: Definições das entidades do banco de dados.
  - `repositories`: Repositórios para acesso aos dados.

- **src/validators**: Contém os validadores para as requisições.
  - `events_creator_validator.py`: Validador para criação de eventos.
  - `subscribers_creator_validator.py`: Validador para criação de inscrições.
  - `events_link_validator.py`: Validador para criação de links de eventos.

## Instalação

1. Clone o repositório:

```sh
git clone https://github.com/akillez01/NLW-Connect-Python.git


```markdown
# NLW Connect Python

Este é um projeto desenvolvido durante o evento NLW Connect, utilizando Python e Flask para criar uma API para gerenciamento de eventos e inscrições.

## Estrutura do Projeto

- **src/main/routes**: Contém as rotas da API.
  - `event.py`: Rotas relacionadas a eventos.
  - `subs.py`: Rotas relacionadas a inscrições.
  - `events_link.py`: Rotas relacionadas a links de eventos.

- **src/controllers**: Contém os controladores que gerenciam a lógica de negócios.
  - `events/events_creator.py`: Lógica para criação de eventos.
  - `subscribers/subscribers_creator.py`: Lógica para criação de inscrições.
  - `subscribers/subscribers_manager.py`: Lógica para gerenciamento de inscrições.
  - `events_link/events_link_creator.py`: Lógica para criação de links de eventos.

- **src/model**: Contém a camada de dados.
  - `configs`: Configurações do banco de dados.
  - `entities`: Definições das entidades do banco de dados.
  - `repositories`: Repositórios para acesso aos dados.

- **src/validators**: Contém os validadores para as requisições.
  - `events_creator_validator.py`: Validador para criação de eventos.
  - `subscribers_creator_validator.py`: Validador para criação de inscrições.
  - `events_link_validator.py`: Validador para criação de links de eventos.

## Instalação

1. Clone o repositório:

```sh
git clone https://github.com/akillez01/NLW-Connect-Python.git
```

2. Navegue até o diretório do projeto:

```sh
cd NLW-Connect-Python
```

3. Crie um ambiente virtual:

```sh
python3 -m venv venv
```

4. Ative o ambiente virtual:

```sh
source venv/bin/activate
```

5. Instale as dependências:

```sh
pip install -r requirements.txt
```

## Execução

Para executar o servidor Flask, utilize o comando:

```sh
python3 run.py
```

O servidor estará disponível em `http://127.0.0.1:3000`.

## Testes

Para executar os testes, utilize o comando:

```sh
pytest -s -v
```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
```