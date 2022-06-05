echo "Insert your Cluster Name : "
read CLUSTER_NAME
echo "- Deleting the Cluster -"

gcloud container clusters delete $CLUSTER_NAME --zone=us-central1-f
echo "- Cluster successfully deleted -"