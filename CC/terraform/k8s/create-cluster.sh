echo "What is youre Project Id ?"
read PROJECT_ID
echo "Setting up the default compute zone.."
gcloud config set project $PROJECT_ID
gcloud config set compute/zone us-central1-f

echo "Insert your Cluster Name : "
read CLUSTER_NAME
echo "Creating a Kubernetes cluster with 3 nodes in the default node pool.."
gcloud beta container clusters create $CLUSTER_NAME \
  --cluster-version=latest \
  --machine-type=n2d-highmem-8 \
  --enable-autoscaling \
  --enable-autorepair \
  --min-nodes=1 \
  --max-nodes=3 \
  --num-nodes=1 \
  --preemptible

echo "Checking that the cluster is up and running.."
gcloud container clusters list
echo "Getting the credentials for you new cluster so you can interact with it using kubectl.."
gcloud container clusters get-credentials $CLUSTER_NAME 
echo "Listing the cluster's nodes.."
kubectl get nodes

echo "Creating new Cloud Storage Bucket.."
export MODEL_BUCKET=${PROJECT_ID}-bucket
gsutil mb gs://${MODEL_BUCKET}
echo "After the bucket has been created copying the model files.."
gsutil cp -r gs://workshop-datasets/models/resnet_101 gs://${MODEL_BUCKET}

echo '"Run terraform file to create configmap, deployment, and service"'
echo '"Then check the services by writing kubectl get svc image-classifier to check the External IP"'
