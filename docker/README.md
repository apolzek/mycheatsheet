
# Docker

## References

| Title                       | URL                                                  |
|-----------------------------|------------------------------------------------------|
| Docker para desenvolvedores | https://github.com/gomex/docker-para-desenvolvedores |


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
docker image list
docker image pull python
docker image inspect python
```

* Run container 
```
docker container run <parameters> <image> <CMD> <args>
```

The parameters most used in the execution of the container are:

| Parameter | Explanation                                                                         |
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

| Parameter | Explanation                                                            |
|-----------|-----------------------------------------------------------------------|
| -a        | Lists all containers, including unconnected ones                      |
| -l        | Lists the latest containers, including unplugged ones                 |
| -n        | Lists the last N containers, including disconnected ones              |
| -q        | List only container ids, great for scripting                          |

```
docker container stop mypython
docker container start mypython

```

---

### Others

* Commonly used
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