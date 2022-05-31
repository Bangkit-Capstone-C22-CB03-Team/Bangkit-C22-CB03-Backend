from locust import HttpUser, task

class ChabotUser(HttpUser):
    @task
    def chatbot_req(self):
        self.client.post("/?msg=What%20percent%20Peru%20hold%20amazon")