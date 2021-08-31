from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1,2)

    @task
    def register_events(self):
        self.client.post(
            "/events/",
            json={
            "session_id": "10e9932e-3c7e-4716-bb69-c8005d1b9661",
            "category": "form interaction",
            "name": "submit",
            "data": {
                "host": "www.ahost.com",
                "path": "/",
                "form": {
                "first_name": "John",
                "last_name": "Doe"
                }
            },
            "timestamp": "2021-01-01 09:15:27.243860"
            },
        )
