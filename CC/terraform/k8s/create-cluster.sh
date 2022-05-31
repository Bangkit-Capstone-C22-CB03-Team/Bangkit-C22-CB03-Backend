echo "-Set the default compute zone-"

PROJECT_ID=<your_project_id>
gcloud config set project $PROJECT_ID
gcloud config set compute/zone us-central1-f

echo "-Set the cluster name-"
CLUSTER_NAME=chatbot-cluster

echo "-Creating a Kubernetes cluster with 3 nodes in the default node pool-"
gcloud beta container clusters create $CLUSTER_NAME \
  --cluster-version=latest \
  --machine-type=n2d-highmem-8 \
  --enable-autoscaling \
  --enable-autorepair \
  --min-nodes=1 \
  --max-nodes=3 \
  --num-nodes=1 \
  --preemptible

# gcloud beta container node-pools create node-pool-1 \
#   --cluster=$CLUSTER_NAME \
#   --machine-type=n2d-highmem-4 \
#   --preemptible \
#   --min-nodes=1 \
#   --max-nodes=3 \
#   --num-nodes=1 \
#   --enable-autoscaling \
#   --enable-autorepair \

echo "-Check that the cluster is up and running-"
gcloud container clusters list

echo "-Get the credentials for you new cluster so you can interact with it using kubectl-"
gcloud container clusters get-credentials $CLUSTER_NAME 

echo "-List the cluster's nodes-"
kubectl get nodes

echo "-Create new bucket-"
export MODEL_BUCKET=${PROJECT_ID}-bucket
gsutil mb gs://${MODEL_BUCKET}

echo "-After the bucket has been created copy the model files-"
gsutil cp -r gs://workshop-datasets/models/resnet_101 gs://${MODEL_BUCKET}

# echo "-Deploying a model-"
# kubectl apply -f tf-serving/configmap.yaml

# echo "Create TF Serving Deployment."
# kubectl apply -f tf-serving/deployment.yaml

# echo "Create TF Serving Service."
# kubectl apply -f tf-serving/service.yaml

echo "-Run terraform file to create configmap, deployment, and service-"
echo "-Then check the services by writing kubectl get svc image-classifier to check the External IP-"
# echo "-Get the external address for the TF Serving service-"
# kubectl get svc image-classifier
