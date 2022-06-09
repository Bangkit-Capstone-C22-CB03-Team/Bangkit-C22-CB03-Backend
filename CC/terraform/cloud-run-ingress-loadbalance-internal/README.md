# To Run the Terraform for cloud-run-ingress-loadbalance-internal

## Prepare the env variable 
```
PROJECT_ID = YOUR_PROJECTID
IMAGE = YOUR_DOCKERIMAGE
```

## To Initialize the Terraform from provider
```
terraform init
```

## To see the terraform detail plan (can be skipped)
```
terraform plan -var=project_id=$PROJECT_ID -var=ingress="internal-and-cloud-load-balancing" -var=image=$IMAGE
```

## To run the terraform implementation please Run
```
terraform apply -var=project_id=$PROJECT_ID -var=ingress="internal-and-cloud-load-balancing" -var=image=$IMAGE
```
