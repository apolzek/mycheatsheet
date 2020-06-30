### Docker

* Most used situations

```
kubectl port-forward kong-kong-<xxx> 8444:8444

docker run -d --name konga --network host -p 1337:1337 pantsel/konga
docker run -d --hostname my-rabbit --name rabbitlocal -p 8080:15672 -p 5672:5672 -p 25676:25676 rabbitmq:3-management
docker exec -it <container_id_or_name> echo "Hello from container!"
```