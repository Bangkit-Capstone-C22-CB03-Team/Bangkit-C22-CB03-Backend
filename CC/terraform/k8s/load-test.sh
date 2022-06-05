kubectl get svc
echo "Insert your service EXTERNAL IP : "
read EXTERNAL_IP

echo "Installing specific locust version.."
pip3 install locust==1.4.1
export PATH=~/.local/bin:$PATH

echo "Configuring Horizontal Pod Autoscaler.."
kubectl autoscale deployment image-classifier \
--cpu-percent=60 \
--min=1 \
--max=4 
echo "Checking the status of the Horizontal Pod Autoscaler.."
kubectl get hpa

echo "Loading test model with Locust.."
cd locust
locust --headless --users 10 --spawn-rate 1 -H http://$EXTERNAL_IP:8080
echo "-Observe the TF Serving Deployment in GKE dashboard.-"

echo '"Your GKE Cluster, deployment & service have been added with HPA"'
echo '"Next try run load-test.sh"'

