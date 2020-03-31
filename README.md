# cheatxit
📑 Cheat sheet for professionals working with technology


## Topics

### Python

* Use venv on Linux (Debian10)
```
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
deactivate
pip install -r requirements.txt
```

### Linux

* Check if port is in use on Linux
```
sudo lsof -i -P -n | grep LISTEN
sudo netstat -tulpn | grep LISTEN
sudo lsof -i:22 ## see a specific port such as 22 ##
sudo ss -tulw
sudo ss -tulwn
sudo nmap -sT -O localhost
sudo nmap -sU -O 192.168.2.13 ##[ list open UDP ports ]##
sudo nmap -sT -O 192.168.2.13 ##[ list open TCP ports ]##

```
