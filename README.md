[![YourActionName Actions Status](https://github.com/hawkz94/gke-k8s-istio/workflows/CI-CD/badge.svg)](https://github.com/hawkz94/gke-k8s-istio/actions)

<h1 align="center">[WIP] GKE - Deploy app using Kubernetes, ISTIO and Github actions</h1>

The objective of this project is to orchestrate a micro-service architecture using Terraform to create the k8s cluster in GKE and managing deployments with k8s and istio.
Integrated with CI/CD Github Actions.

## Dependencies
- [gcloud](https://cloud.google.com/)
- [Terraform](https://learn.hashicorp.com/tutorials/terraform/install-cli)
- [Kubectl](https://kubernetes.io/docs/tasks/tools/)


### WARNING: To proceed with this tutorial you will need to have a GCP account and have your local environment configured with gcloud.

## 1. Create cluster with Terraform:
```
$ cd terraform
$ terraform init
$ terraform apply -y
```

### 1.1 Copy output cmd and exec:
```
$ gcloud container clusters get-credentials my-cluster --zone us-central1-c --project level-gizmo-cxxx
```

#### Verify cluster
```
$ kubeclt get nodes

Output:

NAME                                   STATUS   ROLES    AGE    VERSION
gke-my-cluster-my-pool-d467d8f8-6cpw   Ready    <none>   170m   v1.20.9-gke.701
gke-my-cluster-my-pool-d467d8f8-dhdh   Ready    <none>   170m   v1.20.9-gke.701
gke-my-cluster-my-pool-d467d8f8-n3mk   Ready    <none>   170m   v1.20.9-gke.701
```

## 2. Install ISTIO into cluster:
```
  $ gcloud beta container clusters update my-cluster \
    --update-addons=Istio=ENABLED --istio-config=auth=MTLS_STRICT --zone us-central1-c
```

### 2.1 Inject ISTIO
```
$ kubectl label namespace default istio-injection=enabled --overwrite
```

## 3. Install Cert Manager into cluster:
```
 $ kubectl apply -f https://github.com/jetstack/cert-manager/releases/download/v1.5.3/cert-manager.yaml
```

## 4. Apply ISTIO Ingress and deployment app:
```
 $ kubectl apply -f k8s/isito-gateway.yml
 $ kubectl apply -f k8s/deployment.yml

## Author
- Harrisson Ricardo Biaggio
```
