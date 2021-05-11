
# AWS CLI

## References

| Title                       | URL                                                                             |
|-----------------------------|---------------------------------------------------------------------------------|
| Docs EKS(pt-br)             | https://docs.aws.amazon.com/pt_br/eks/latest/userguide/eks-ug.pdf               |

### Commands

#### First Steps

```
aws configure
```

#### EKS

:heavy_dollar_sign: fargate

```
eksctl create cluster \
--name my-cluster \
--region us-west-2 \
--fargate

```

:heavy_dollar_sign: managed

```
aws ec2 create-key-pair --region us-west-2 --key-name myKeyPair

eksctl create cluster \
--name my-cluster \
--region us-west-2 \
--with-oidc \
--ssh-access \
--ssh-public-key <your-key> \
--managed
```

```
# Delete cluster EKS
eksctl delete cluster --name my-cluster --region us-west-2
```