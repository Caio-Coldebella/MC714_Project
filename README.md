# MC714 - project

## Dependências 
Para todos os algoritmo temos um arquivo requirements.txt. Para baixar e instalar as dependências necessárias para rodar o projeto localmente rode o comando *pip install -r requirements.txt*

## Como rodar cara servidor:
### LeaderElection:
Nesse pacote temos dois arquivos que sobem servidores, o server.py e o server_test.py.

**server_test.py**: Ele sobe um servidor no localhost apenas alterando a porta dado o comando de execução.
Para executar basta rodar *python3 server_test.py 1*
Para ver o funcionamento da eleição de lider basta subir outros servidores locais em outras portas:

*python3 server.py 1*

*python3 server.py 2*

*python3 server.py 3*

**serve.py**: Esse foi o programa usado na apresentação do trabalho, pois nele já contêm os ips das máquinas virtuais que subimos na GCP. 
As três máquinas tinham esse projeto clonado com as dependências já instaladas.

### Lamport
Nesse pacote temos dois arquivos que sobem servidores, o server.py e o server_test.py.

**server_test.py**: Ele sobe um servidor no localhost apenas alterando a porta dado o comando de execução.
Para executar basta rodar *python3 server_test.py --frequency=2 --address=50051*.
Para ver o funcionamento basta subir outros servidores em outras portas e se quiser com frequencias diferentes.

*python3 server_test.py --frequency=2 --address=50051*

*python3 server_test.py --frequency=2 --address=50052*

*python3 server_test.py --frequency=2 --address=50053*

**serve.py**: Esse foi o programa usado na apresentação do trabalho, pois nele já contêm os ips das máquinas virtuais que subimos na GCP. 
As três máquinas tinham esse projeto clonado com as dependências já instaladas.

### MutualExclusion

