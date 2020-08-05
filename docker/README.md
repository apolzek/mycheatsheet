
# Docker

## Referências

| Título                      | URL                                                  |
|-----------------------------|------------------------------------------------------|
| Docker para desenvolvedores | https://github.com/gomex/docker-para-desenvolvedores |


### Instalar Docker engine no GNU/Linux (sudo)
```
wget -qO- https://get.docker.com/ | sh
wget -qO- https://get.docker.com/gpg | sudo apt-key add -
pip install docker-compose
```

### Instalar Docker machine no GNU/Linux (sudo)
```
curl -L https://github.com/docker/machine/releases/download/v0.10.0/docker-machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine && \
chmod +x /usr/local/bin/docker-machine
docker-machine version
```

### Comandos básicos
```
docker image list
docker image pull python
docker image inspect python
```

* Rodar um container 
```
docker container run <parâmetros> <imagem> <CMD> <argumentos>
```

Os parâmetros mais utilizados na execução do contêiner são:

| Parâmetro | Explicação                                                                    |
|-----------|-------------------------------------------------------------------------------|
| -d        | Execução do contêiner em background                                           |
| -i        | Modo interativo. Mantém o STDIN aberto mesmo sem console anexado              |
| -t        | Aloca uma pseudo TTY                                                          |
| --rm      | Automaticamente remove o contêiner após finalização (**Não funciona com -d**) |
| --name    | Nomear o contêiner                                                            |
| -v        | Mapeamento de volume                                                          |
| -p        | Mapeamento de porta                                                           |
| -m        | Limitar o uso de memória RAM                                                  |
| -c        | Balancear o uso de CPU                                                        |


```
docker container run -it --rm --name meu_python python bash
docker container run -it --rm -v "<host>:<container>" python

docker container run -it --rm -p "<host>:<container>" python
docker container run -it --rm -p 80:8080 python

docker container run -it --rm -m 512M python
docker container run -it --rm -c 512 python
```

* Listar containers
```
docker container ls <parâmetros>
```

Os parâmetros mais utilizados na execução do contêiner são:

| Parâmetro | Explicação                                                            |
|-----------|-----------------------------------------------------------------------|
| -a        | Lista todos os contêineres, inclusive os desligados                   |
| -l        | Lista os últimos contêineres, inclusive os desligados                 |
| -n        | Lista os últimos N contêineres,  inclusive os desligados              |
| -q        | Lista apenas os ids dos contêineres, ótimo para utilização em scripts |

```
docker container stop meu_python
docker container start meu_python

```

---

### Outros

* Mais usados

```
docker run -d --name konga --network host -p 1337:1337 pantsel/konga
docker run -d --hostname my-rabbit --name rabbitlocal -p 8080:15672 -p 5672:5672 -p 25676:25676 rabbitmq:3-management
docker exec -it <container_id_or_name> echo "Hello from container!"
```

* Troubleshooting

```
docker run busybox ping -c 1 192.203.230.10
docker run busybox nslookup google.com
nmcli dev show | grep 'IP4.DNS'
docker run --dns 10.0.0.2 busybox nslookup google.com

/etc/docker/daemon.json
{
    "dns": ["10.0.0.2", "8.8.8.8"]
}
sudo service docker restart
docker run busybox nslookup google.com

```