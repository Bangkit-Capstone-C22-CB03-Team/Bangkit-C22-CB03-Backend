kubectl get svc
EXTERNAL_IP=<service_external_ip>
echo "-Install specific locust version-"
pip3 install locust==1.4.1
export PATH=~/.local/bin:$PATH
# echo "Verify that the model is up and operational."
# curl -d @locust/request-body.json -X POST http://$EXTERNAL_IP:8501/v1/models/image_classifier:predict


echo "Configure Horizontal Pod Autoscaler."
kubectl autoscale deployment image-classifier \
--cpu-percent=60 \
--min=1 \
--max=4 

echo "Check the status of the autoscaler."
kubectl get hpa

echo "-Your k8s Cluster, deployment, service have been added with Horizontal Pod Autoscaling-"
echo "-Next try run load-test-model.sh for-"

echo "Load test the model"
cd locust
locust --headless --users 10 --spawn-rate 1 -H http://$EXTERNAL_IP:8080
# locust -f tasks.py \
# --headless \
# --host http://${EXTERNAL_IP}:8501

# locust -f tasks.py \
# --headless \
# --host http://${EXTERNAL_IP}:8080

# cd locust
# locust -f tasks.py --headless --users 32 --spawn-rate 1 --step-load --step-users 1 --step-time 30s --host http://$EXTERNAL_IP:8501

echo "-Observe the TF Serving Deployment in GKE dashboard.-"
echo "-Observe the default node-pool-"