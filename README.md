# Expense Tracker

Este é um projeto de rastreamento de despesas simples escrito em Python. Ele permite que você adicione, liste, exclua e resuma suas despesas.

- https://roadmap.sh/projects/expense-tracker

## Funcionalidades

- Adicionar uma nova despesa com descrição e valor.
- Listar todas as despesas.
- Excluir uma despesa pelo ID.
- Mostrar um resumo total das despesas, opcionalmente filtrado por mês.

## Requisitos

- Python 3.x

## Instalação

Clone o repositório e navegue até o diretório do projeto:

```bash
git clone https://github.com/seu-usuario/expense-tracker.git
cd expense-tracker
```

## Uso

### Adicionar uma despesa

```bash
python expense_tracker.py add --description "Descrição da despesa" --amount 100.50
```

### Listar todas as despesas

```bash
python expense_tracker.py list
```

### Excluir uma despesa

```bash
python expense_tracker.py delete --id 1
```

### Mostrar o resumo das despesas

```bash
python expense_tracker.py summary
```

### Mostrar o resumo das despesas de um mês específico

```bash
python expense_tracker.py summary --month 1
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.