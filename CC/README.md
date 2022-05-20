# instructions
how to build docker images :
in 
```bash 
cd Bangkit-C22CB-Company-Based-Capstone/CC
docker build -t chatbot-traveloka:0.1 .
```
it will build ubuntu server and all the app configurations in Dockerfile

check if the docker image built successfully.
```bash
docker images
```
run the docker image to the container by writing this command
```bash
docker run -p 8080:8080 chatbot:0.1
```
or for naming it :
```bash
docker run -p 8080:8000 --name chatbot-traveloka chatbot:0.1
```
check if it run successfully on port 8080
```bash
curl http://localhost:8080 | curl http://0.0.0.0:8080
```
to get inside the server / container use this command :
```bash
docker exec -it [container_id] bash | docker exec -it [container_id] sh
ls
exit
```

