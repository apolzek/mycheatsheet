
# Docker / Docker Swarm :whale2:

## References

| Title                       | URL                                                                             |
|-----------------------------|---------------------------------------------------------------------------------|
| Docs                        | https://docs.docker.com/                                                        |
| Docker para desenvolvedores | https://github.com/gomex/docker-para-desenvolvedores                            |
| Curso de Docker Completo    | [URL](https://www.youtube.com/playlist?list=PLg7nVxv7fa6dxsV1ftKI8FAm4YD6iZuI4) |

### Install Docker

* https://docs.docker.com/get-docker/
* https://docs.docker.com/compose/install/
* https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/
* https://docs.docker.com/machine/install-machine/

### Install Docker Engine on GNU / Linux (sudo required)

```
wget -qO- https://get.docker.com/ | sh
wget -qO- https://get.docker.com/gpg | sudo apt-key add -
pip install docker-compose
```

### Install Docker Machine on GNU / Linux (sudo required)
```
curl -L https://github.com/docker/machine/releases/download/v0.10.0/docker-machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine && \
chmod +x /usr/local/bin/docker-machine
docker-machine version
```

### Basic commands
```
# Version / Shows if you have client and server
docker version 

# Overview Docker on the machine
docker info

docker image list
docker image pull IMAGE_ID (Ex: docker image pull python)
docker image inspect IMAGE_ID (Ex: docker image inspect postgres:12.2)
```

* Run container 
```
docker container run <parameters> <image> <CMD> <args>
```

The parameters most used in the execution of the container are:

| Parameter | Explanation                                                                        |
|-----------|------------------------------------------------------------------------------------|
| -d        | Container execution in the background                                              |
| -i        | Interactive mode. Keeps STDIN open even without a console attached                 |
| -t        | Allocates a pseudo TTY                                                             |
| --rm      | Automatically removes the container after completion (** Does not work with -d **) |
| --name    | Name                                                                               |
| -v        | Volume mapping                                                                     |
| -p        | Port mapping                                                                       |
| -m        | Limit the use of RAM                                                               |
| -c        | Balance CPU usage                                                                  |

```
docker container run -it --rm --name mypython python bash
docker container run -it --rm -v "<host>:<container>" python

docker container run -it --rm -p "<host>:<container>" python
docker container run -it --rm -p 80:8080 python

docker container run -it --rm -m 512M python
docker container run -it --rm -c 512 python
```

* List containers
```
docker container ls <parameters>
```

The parameters most used in the execution of the container are:

| Parameter | Explanation                                              |
|-----------|----------------------------------------------------------|
| -a        | Lists all containers, including unconnected ones         |
| -l        | Lists the latest containers, including unplugged ones    |
| -n        | Lists the last N containers, including disconnected ones |
| -q        | List only container ids, great for scripting             |


* Remove all containers/images
```
docker rm $(docker ps -a -q) -f
docker rmi -f $(docker images -a -q)
```

* View container processes/ consume/ info
```
docker container top ID_OR_NAME 
docker container stats
docker container stats ID_OR_NAME
docker container inspect ID_OR_NAME
docker container inspect -f {{.NetworkSettings}} ID_OR_NAME
```

* Inspect
```
# Get an instance’s IP address
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $INSTANCE_ID 
(Output ex: 172.17.0.2)

# Get an instance’s MAC address
docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' $INSTANCE_ID
(Output ex: 02:42:ac:11:00:02)

# Get an instance’s log path
docker inspect --format='{{.LogPath}}' $INSTANCE_ID

# Get an instance’s image name
docker inspect --format='{{.Config.Image}}' $INSTANCE_ID

# List all port bindings
docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' $INSTANCE_ID
(Output ex: 80/tcp -> 80)
```

* Stop and Start containers
```
docker container stop mypython
docker container start mypython
```

* Create image
```
docker container run -it --name containerxyz ubuntu:16.04 bash

apt-get update
apt-get install nginx -y
exit

docker container stop containerxyz

docker container commit containerxyz myubuntu:nginx
docker container run -it --rm myubuntu:nginx dpkg -l nginx
```

* Dockerfile and build image
```
FROM ubuntu:16.04
RUN apt-get update && apt-get install nginx -y
COPY testfile /tmp/testfile
CMD bash
```

```
docker image build -t myubuntu:nginx_auto .
```

* Dockerhub/Images
```
docker tag docker-is-cool DOCKER_ID/docker-is-cool:latest
docker login
docker image push
docker images rm -f IMAGE_ID
docker rmi -f IMAGE_ID
```

* Volumes
```
# Requires the host to have a specific folder for the container to function properly
docker container run -v /var/lib/containerx:/var ubuntu
```

```
docker create -v /dbdata --name dbdata postgres /bin/true
docker container run -d --volumes-from dbdata --name db2 postgres
```

```
docker volume create --name dbdata
docker container run -d -v dbdata:/var/lib/data postgres
```

* Network 
```
# Bridge => Internal communication between containers, Standard network 172.17.0.0/16
# Host => You don't need to publish a door. Does not work in swarm mode
# None => Does not have external access or with other containers

iptables -t nat -L

docker network ls
docker network inspect NETWORK_NAME

docker container run -d --name db -e MYSQL_ROOT_PASSWORD=myp@ss mysql
docker container run -d -p 80:80 --name app --link db tutum/apache-php
docker container run -d -P nginx # Publish port randomly
docker container exec -it app ping db

docker container run --name net_host1 -d --network host nginx:alpine
docker container run -d --name h_none --network none nginx:alpine
docker network create my_custom_net --subnet 192.168.134.0/24 --gateway 192.168.134.1
docker container run --name webhost -d --network my_custom_net nginx
docket network prune
docker network connect NETWORK_NAME CONTAINER_ID_OR_NAME
```

* Dockerhub 
```
docker build -t <your_username>/my-first-repo . 
docker run <your_username>/my-first-repo
docker push <your_username>/my-first-repo
```

---

### Troubleshooting


* Useful commands

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
```
---

### Docker Swarm

* Basic commands

```
# Set up master
docker swarm init --advertise-addr <ip>   

# Force manager on broken cluster
docker swarm init --force-new-cluster -advertise-addr <ip>   

# Get token to join workers
docker swarm join-token worker

# Get token to join new manager
docker swarm join-token manager           

# Join host as a worker
docker swarm join <server> worker

docker swarm leave

docker swarm unlock                       

# Print key needed for 'unlock'
docker swarm unlock-key                   

# Print swarm node list
docker node ls                           
docker node rm <node id>
docker node inspect --pretty <node id>
docker node update <node> --availability active

# Promote node to manager
docker node promote <node id>             

# Rebalancing
for svc in $(docker service ls -q) ; do docker service update $svc --force ; done

# Force restart
for i in $(docker service ls | grep 0/ | awk '{print $2}'); do docker service update --force $i; done

docker stack ls
docker stack rm <name>

docker service create <image>
docker service create --name <name> --replicas <number of replicas> <image>
docker service scale <name>=<number of replicas>
docker service rm <service id|name>

# List all services
docker service ls                        

# List all tasks for given service (includes shutdown/failed)                            
docker service ps <service id|name>                                 

# List running (acitve) tasks for given service
docker service ps --filter desired-state=running <service id|name>   

# Print console log of a service
docker service logs --follow <service id|name>
```

---

### Most used services

```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
docker run -d --hostname my-rabbit --name rabbitlocal -p 8080:15672 -p 5672:5672 -p 25676:25676 rabbitmq:3-management
docker run --rm --name mongodb -p 27017:27017 mongo:latest
docker run -d --name konga --network host -p 1337:1337 pantsel/konga
docker run -d -p 3000:3000 --name grafana grafana/grafana:6.5.0
docker run -it -v $PWD:/app -w /app --entrypoint "" hashicorp/terraform:light sh
```
