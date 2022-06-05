create cluster & cloud storage bucket with tensorflow model by running create-cluster bash file
```
sh create-cluster.sh
```
run terraform to create configmap and pull the model from cloud storage bucket that we built before
```
cd deployments
terraform init
terraform plan
terraform apply
```
configure EXTERNAL_IP=<service_external_ip> in load-test-model.sh

you can find the EXTERNAL_IP by writing this command to get all running services
```
kubectl get svc
```
create HPA(Horizontal Pod Autoscaling) & test the model.
```
sh load-test.sh
```