# Arquitetura do Sistema Mãos Solidárias

## 1. Visão geral

O projeto prevê o desenvolvimento de um sistema web para organizar o cadastro de famílias, as entregas de cestas básicas e o estoque de alimentos.

## 2. Arquitetura escolhida

Será utilizada uma arquitetura monolítica, organizada em três camadas:

- Apresentação: telas e formulários utilizados pelos voluntários.
- Regras de negócio: validação dos cadastros, entregas e estoque.
- Persistência: armazenamento das informações no banco de dados.

## 3. Tecnologias previstas

- Python 3.12
- Django 5.2 LTS
- HTML5 e CSS3
- Bootstrap 5.3
- PostgreSQL

## 4. Organização dos dados

O sistema terá quatro entidades principais:

- Família: informações necessárias ao atendimento.
- Entrega: registro das cestas distribuídas.
- Produto: alimentos disponíveis no estoque.
- Movimentação de Estoque: entradas e saídas de produtos.

## 5. Regras principais

- Cada família poderá receber uma cesta por mês.
- O sistema deverá impedir entregas duplicadas.
- As entregas deverão respeitar a disponibilidade do estoque.
- O acesso às informações será restrito a usuários autorizados.

## 6. Segurança e acessibilidade

O sistema deverá utilizar autenticação, validação de dados e proteção das informações cadastradas.

A interface será responsiva, com botões grandes, textos legíveis e mensagens de erro compreensíveis.

## 7. Objetivo social

O projeto está alinhado ao ODS 2 - Fome Zero e Agricultura Sustentável, buscando melhorar a organização da distribuição de alimentos e reduzir desperdícios.
