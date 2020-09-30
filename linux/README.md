
### Linux

* Find/ Remove

```
sudo find ./ -iname "<file-name>*" -exec rm {} \;
```

* Check if port is in use on Linux

```
cat /etc/services
grep -w '443/tcp' /etc/services
egrep -w '22/(tcp|udp)' /etc/services

fuser -k 8080/tcp
sudo lsof -i -P -n | grep LISTEN
sudo netstat -tulpn | grep LISTEN
sudo lsof -i:22 ## See a specific port such as 22
sudo lsof -nP -iTCP -sTCP:LISTEN
sudo watch ss -tulpn
sudo ss -tulw
sudo ss -tulwn 
# -t : Show only TCP sockets on Linux
# -u : Display only UDP sockets on Linux
# -l : Show listening sockets. For example, TCP port 22 is opened by SSHD server.
# -p : List process name that opened sockets
# -n : Don’t resolve service names i.e. don’t use DNS
sudo nmap -sT -O localhost
sudo nmap -sU -O 192.168.2.13 # List open UDP ports
sudo nmap -sT -O 192.168.2.13 # List open TCP ports 
```

* Check and list active SSH connections in Linux

```
ss | grep -i ssh
last -a | grep -i still
who
w
netstat -tnpa | grep 'ESTABLISHED.*sshd'
ps auxwww | grep sshd: | grep -v grep
```

* dpkg/.deb

```
dpkg -l # List installed packages
dpkg -s mypkg # Get status of specific package

apt list --installed # List installed packages
apt list # List *all* packages in available repos
dpkg -b ./mypkg ./mypkg_1.0.0-0_amd64.deb
dpkg -I mypkg.deb # Inspect information 
dpkg -c mypkg.deb # Review the contents
dpkg -X mypkg.deb /tmp/exctact/ # Extract the contents
sudo apt install ./mypkg.deb # Install 
sudo dpkg -i mypkg.deb # Install
dpkg --remove package_name # Leaves config files
dpkg --purge package_name  # Removes config files too

# Structure for a package
mypkg/             # Directory
├── DEBIAN/        # Directory
│   └── control    # Control file
│   └── postinst   # Post install script
├── etc/my.ini     # Optionally any other files that you need to include
└── opt/mylib/     # on the destination system during installation

# This is a minimal example of the DEBIAN/control file:
-
Package: mypkg
Version: 1.0.0
Maintainer: Your Name <you@example.com>
Description: My test package, please ignore
Homepage: https://github.com/username/projectname
Architecture: all
Depends: git, python3 (>=3.5), openjdk-8-jre-headless|openjdk-8-jre|openjdk-8-jdk-headless|openjdk-8-jdk
-

# Convert a .deb to .rpm and other formats
sudo apt install alien
alien --help
alien --to-rpm my_pkg.deb
```

* PPA

```
sudo add-apt-repository --remove ppa:<ppa_name>/ppa
sudo ls /etc/apt/sources.list.d
sudo rm -i /etc/apt/sources.list.d/<ppa_name.list>
```
* Generate A Strong Password In Linux

```
openssl rand -base64 14 # 6iILGKjgCPc13mQo/jo=
cat /dev/urandom | tr -dc a-zA-Z0-9 | fold -w 14 | head -n 1 # xGp9LIzsaoJcZ5
< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c${1:-32};echo; # _e0EZFl48koBBqTCe4WT43jdXqq7NHQ1
tr -cd '[:alnum:]' < /dev/urandom | fold -w30 | head -n1 # 0oZYBhvsqvJ9hPzCNg7zgskNaedXCm
strings /dev/urandom | grep -o '[[:alnum:]]' | head -n 30 | tr -d '\n'; echo # aiZEtYlkCgBUrBdZJKMr1wovgjM4Go
< /dev/urandom tr -dc _A-Z-a-z-0-9 | head -c6 # Jzjyar
dd if=/dev/urandom bs=1 count=32 2>/dev/null | base64 -w 0 | rev | cut -b 2- | rev # z2VFL+nCKNOlmxTucy9BhehzNqS/uGmAQEvDpubJHDk
</dev/urandom tr -dc '12345!@#$%qwertQWERTasdfgASDFGzxcvbZXCVB' | head -c8; echo "" # xT%eV1WR

sudo apt install pwgen
pwgen 14 1 # AhchohNukoop8X

```

* FTP upload 

```
curl -T my-local-file.txt ftp://ftp.example.com --user user:secret
ftp-upload -h {HOST} -u {USERNAME} --password {PASSWORD} -d {SERVER_DIRECTORY} {FILE_TO_UPLOAD}
```

* Passwordless SSH on Ubuntu and CentOS:

```
ssh-keygen -t rsa
ssh-keygen -t rsa -b 4096
ssh-copy-id <remote_user>@<remote_ip>
```
IP/Networking

```
hostname -I | awk '{print $1}'
```
Name file manager
xdg-mime query default inode/directory 


* Recursos de maquina

```
 ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head
````

---

## Others


```
#fuser centos
yum install psmisc
```

