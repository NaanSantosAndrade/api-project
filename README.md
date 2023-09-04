# Projeto Bootcamp Santander

## Introdução
Este é um projeto para o Módulo de Introdução a Ciência de Dados do Bootcamp Santander 2023

A utilização da temática de Pokemon é porque foi fácil de encontrar uma database em CSV 🙃

Aqui o objetivo é criar um simples ETL (Extract, Transform, Load) e aproveitando a oportunidade estudei para desenvolver minhas próprias APIs.
Com o tempo irei aprimorar as boas práticas do projeto e da documentação.

## Documentação
Google Colab ETL Project:
https://colab.research.google.com/drive/11CkrdkccuaoOw1ANWIdF-cqN2WKN27Mz#scrollTo=HLN0iDgThgyK

1. Instale o NGROK https://ngrok.com/download
Este projeto cria um servidor Localhost, com o NGROK você conseguirá criar uma URL pública do servidor local para o Google Colab poder acessar.
2. Inicialize o arquivo main.py para levantar o Servidor na porta 80
3. Siga os passos da documentação de inicialização do ngrok.exe: https://dashboard.ngrok.com/get-started/setup
4. Agora você está livre para utilizar o Google Colab: https://colab.research.google.com/drive/11CkrdkccuaoOw1ANWIdF-cqN2WKN27Mz#scrollTo=HLN0iDgThgyK

PS: Se você receber o erro do NGROK: "Your account is limited to 1 simultaneous ngrok agent session" tente utilizar os seguintes comandos para reiniciar as tarefas:
- taskkill /f /im ngrok.exe
- ngrok http 80
