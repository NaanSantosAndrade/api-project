# api-project

Google Colab ETL Project:
https://colab.research.google.com/drive/11CkrdkccuaoOw1ANWIdF-cqN2WKN27Mz#scrollTo=HLN0iDgThgyK

1. Instale o NGROK https://ngrok.com/download
Este projeto cria um servidor Localhost, com o NGROK você conseguirá criar uma URL pública do servidor local para o Google Colab poder acessar.
2. Inicialize o arquivo main.py para levantar o Servidor na porta 80
3. Siga os passos da documentação de inicialização do ngrok.exe: https://dashboard.ngrok.com/get-started/setup
4. Agora você está livre para utilizar o Google Colab: https://colab.research.google.com/drive/11CkrdkccuaoOw1ANWIdF-cqN2WKN27Mz#scrollTo=HLN0iDgThgyK

PS: Se você receber o erro do NGROK: "Your account is limited to 1 simultaneous ngrok agent session" tente utilizar os seguntes comandos:
- taskkill /f /im ngrok.exe
- ngrok http 80
