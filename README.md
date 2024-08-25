# Sistema Bancário - Projeto DIO NTT Data

Este projeto é uma aplicação de console em Python que simula um sistema bancário simples.<br>
O objetivo é permitir que os usuários realizem operações básicas como depósito, saque e consulta de extrato, respeitando limites de saldo e número de saques.

## Descrição Geral

A aplicação oferece uma interface interativa via linha de comando, onde o usuário pode escolher entre diferentes opções<br>
para manipular sua conta bancária. Cada operação é gerida através de um loop que permanece ativo até que o usuário decida sair.

## Estrutura do Projeto

O projeto é composto de um único arquivo Python (`main.py`) que contém toda a lógica necessária para a simulação do sistema bancário.

## Funcionalidades

1. **Depósito**:
   - O usuário pode depositar um valor positivo na conta.
   - O saldo da conta é atualizado e o valor é registrado no extrato.

2. **Saque**:
   - O usuário pode realizar saques desde que o valor não exceda o saldo disponível,<br>
   o limite diário de R$ 500,00 ou o número máximo de 3 saques por dia.
   - O saldo é atualizado e o saque é registrado no extrato.

3. **Extrato**:
   - O usuário pode visualizar o extrato das operações realizadas.
   - Se não houver movimentações, uma mensagem informativa será exibida.
   - O saldo atual também é mostrado.

4. **Sair**:
   - O usuário pode encerrar a aplicação a qualquer momento escolhendo a opção de sair no menu do sistema.

---

Obrigada por conferir o projeto do Sistema Bancário! 💰
