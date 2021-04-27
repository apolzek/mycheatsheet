
# Docker / Docker Swarm :whale2:

## References

| Title                       | URL                                                                             |
|-----------------------------|---------------------------------------------------------------------------------|
| Docs                        | https://docs.docker.com/                                                        |
| Docker para desenvolvedores | https://github.com/gomex/docker-para-desenvolvedores                            |
| Curso de Docker Completo    | [URL](https://www.youtube.com/playlist?list=PLg7nVxv7fa6dxsV1ftKI8FAm4YD6iZuI4) |
| Install docker-compose      |  https://docs.docker.com/compose/install/                                       |

### Commands

#### Info

```
# Version(Client/Server)
docker version 

# Overview Docker on the machine
docker info
```

#### Images

:heavy_dollar_sign: general

```
# List all images
docker image list
docker image ls

docker image pull <IMAGE_ID_OR_NAME>:<TAG>
$ docker image pull python:2.7

docker image inspect <IMAGE_ID_OR_NAME>
$ docker image inspect python:2.7

docker image history <IMAGE_ID_OR_NAME>:<TAG>
$ docker image history python:latest

docker image rm <IMAGE_ID_OR_NAME>:<TAG> -f
$ docker image rm python:latest -f

# Remove all images
docker rmi -f $(docker images -a -q)
```

:heavy_dollar_sign: create image(commit mode)

```
docker container run -it --name <NAME_YOU_CHOSE> ubuntu:16.04 bash
$ docker container run -it --name example ubuntu:16.04 bash

apt-get update
apt-get install nginx -y
(crtl p + q)

docker container stop <NAME_YOU_CHOSE>
$ docker container stop example

docker container commit <NAME_YOU_CHOSE> <NEW_NAME_YOU_CHOSE>:<TAG>
$ docker container commit example new_example:latest

docker container run -it --rm <NEW_NAME_YOU_CHOSE>:<TAG> dpkg -l nginx
$ docker container run -it --rm new_example:latest dpkg -l nginx

```

#### Container

:heavy_dollar_sign: container run
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
docker container run -it --rm --name <NAME> <IMAGE> <COMMAND>
$ docker container run -it --rm --name python python bash

docker run -d -it --name <NAME> --mount type=bind,source="<LOCAL_FOLDER>",target=<CONTAINER_FOLDER> <IMAGE>:<TAG>
$ docker run -d -it --name example --mount type=bind,source="$(pwd)",target=/app nginx:latest

docker run -d -it --name example -v "<LOCAL_FOLDER>":/<CONTAINER_FOLDER> <IMAGE>:<TAG>
$ docker run -d -it --name example -v "$(pwd)":/app nginx:latest

docker container run -it --rm -p "<HOST_PORT>:<CONTAINER_PORT>" <IMAGE>:<TAG>
$ docker container run -it --rm -d -p 8080:80 nginx:latest

# Limit memory
docker container run -it --rm -m <SIZE>M <IMAGE>:<TAG>
$ docker container run -it --rm -m 512M apline:latest

# Limit cpu
docker container run -it --rm -c <SIZE> <IMAGE>:<TAG>
$ docker container run -it --rm -c 512 alpine:latest

# Check cpu limit
docker container inspect -f {{.HostConfig.CpuShares}} <CONTAINER_ID_OR_NAME> 
$ docker container inspect -f {{.HostConfig.CpuShares}} 49ecaa5707b5
```

:heavy_dollar_sign: container ls 

```
docker container ls <parameters>
```

The most used parameters in the container listing are:

| Parameter | Explanation                                              |
|-----------|----------------------------------------------------------|
| -a        | Lists all containers, including unconnected ones         |
| -l        | Lists the latest containers, including unplugged ones    |
| -n        | Lists the last N containers, including disconnected ones |
| -q        | List only container ids, great for scripting             |

```
docker container ls -a

docker container ls -n <NUMBER>
$ docker container ls -n 1

docker container ls -1

# Remove all containers
docker rm $(docker ps -a -q) -f 2>/dev/null  || echo "0 containers running" 
```

:heavy_dollar_sign: view container processes, consume and info

```
docker container top <CONTAINER_NAME_OR_ID>

docker container stats
docker container stats <CONTAINER_NAME_OR_ID>

```

:heavy_dollar_sign: inspect

```
docker container inspect <CONTAINER_NAME_OR_ID>
docker container inspect -f {{.NetworkSettings}} <CONTAINER_NAME_OR_ID>
$ docker container inspect -f {{.NetworkSettings}} festive_elbakyan

# Get an instance’s IP address
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <CONTAINER_NAME_OR_ID>

# Get an instance’s MAC address
docker inspect --format='{{range .NetworkSettings.Networks}}{{.MacAddress}}{{end}}' <CONTAINER_NAME_OR_ID>

# Get an instance’s log path
docker inspect --format='{{.LogPath}}' <CONTAINER_NAME_OR_ID>

# Get an instance’s image name
docker inspect --format='{{.Config.Image}}' <CONTAINER_NAME_OR_ID>

# List all port bindings
docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' <CONTAINER_NAME_OR_ID>
```

:heavy_dollar_sign: stop/start containers
```
docker container stop <CONTAINER_NAME_OR_ID>
docker container start <CONTAINER_NAME_OR_ID>
```

#### Dockerfile

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


### Alias