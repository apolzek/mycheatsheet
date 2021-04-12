
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
