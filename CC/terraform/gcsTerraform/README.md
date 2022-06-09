# To Run the Terraform for Google Cloud Storage bucket

## Prepare the env variable 
```
PROJECT_ID = YOUR_PROJECTID
```

## To Initialize the Terraform from provider
```
terraform init
```

## To see the terraform detail plan (can be skipped)
```
terraform plan -var=project_id=$PROJECT_ID
```

## To run the terraform implementation please Run
```
terraform apply -var=project_id=$PROJECT_ID
```
