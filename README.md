# MC714 - 2° Trabalho

## Instalação das Dependências 
Para todos os algoritmos, há um arquivo requirements.txt. Para baixar e instalar as dependências necessárias para rodar o projeto localmente execute o comando *pip install -r requirements.txt*

# Algoritmo de Eleição de Líder:

Os arquivos *server_test.py* e *serve.py* foram iniciados em VMs do GCP.

**server_test.py**: Arquivo que inicia um servidor no localhost, alterando a porta quando dado um o comando de execução.
Para executar basta rodar *python3 server_test.py 1*
Para ver o funcionamento da eleição de lider basta iniciar outros servidores locais em outras portas:

*python3 server.py 1*

*python3 server.py 2*

*python3 server.py 3*

**serve.py**: Este programa foi utilizado na apresentação do trabalho, e contêm os IPs das VMs que foram iniciadas no GCP. 
As três máquinas foram executadas com este projeto clonado com as dependências já instaladas.

# Relógio Lógico de Lamport

Os arquivos *server.py* e *server_test.py* foram iniciados em VMs do GCP.

**server_test.py**: Arquivo que inicia um servidor no localhost, alterando a porta quando dado o comando de execução.
Para executar basta rodar *python3 server_test.py --frequency=2 --address=50051*.
Para ver o funcionamento basta iniciar outros servidores em outras portas, opcionalmente com frequências de clock diferentes,
afim de ser possível observar a dessincronização dos relógios em diferentes servidores.

*python3 server_test.py --frequency=2 --address=50051*

*python3 server_test.py --frequency=2 --address=50052*

*python3 server_test.py --frequency=2 --address=50053*

**serve.py**: Este foi o programa utilizado na apresentação do trabalho, pois nele já estão contidos os IPs das VMs que foram iniciadas no GCP. 
As três máquinas foram executadas com este projeto clonado com as dependências já instaladas.

# Algoritmo de Exclusão Mútua

## Descrição

A implementação do algoritmo de exclusão mútua foi realizada utilizando containeres Docker, com um container sendo o Lock Manager,
o qual detêm o controle do lock, e containeres clientes, que pedem acesso ao lock e utilizam o recurso por um determinado tempo.
Os clientes pedem acesso ao recurso repetidamente a cada X segundos, definido de forma aleatória. A comunicação entre os clientes
e o Lock Manager foi feita através do RabbitMQ, e foi utilizado [Direct Exchange](https://www.rabbitmq.com/tutorials/tutorial-four-python)
para gerenciar os canais das mensagens dos clientes e do manager separadamente, de forma que cada consumidor tivesse acesso apenas às mensagens
endereçadas à este. Quando o Lock Manager não pode liberar o lock para um cliente, o cliente entra em um estado de espera e o Lock Manager
adiciona a requisição novamente à fila.

## Execução do Programa

Inicie o container do Lock Manager a partir do arquivo *docker-compose.yml*

```
sudo docker compose up
```

Após a criação do container, será mostrada a mensagem *Lock manager started*, em seguida inicie os clientes a partir do script *run.bash*

```
sudo bash run.bash
```