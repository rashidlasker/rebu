from locust import HttpLocust, TaskSet

def login(l):
    response = l.client.get('/login/')
    csrftoken = response.cookies['csrftoken']
    l.client.post("/login", {"username":"yeet", "password":"password"}, headers={'X-CSRFToken': csrftoken})

def logout(l):
    l.client.post("/logout")

def index(l):
    l.client.get("/")

def search(l):
    l.client.get("/search?query=steak")

def meal(l):
    l.client.get("/meals/2/")

def create_meal(l):
    response = l.client.get('/login/')
    csrftoken = response.cookies['csrftoken']
    l.client.post("/login", {'tags': 'asian savory meat', 'cook': 1, 'description': 'gruyere-thyme potatoes, tamari-ginger pan sauce', 'name': 'Steak Chinoise', 'calories': 100, 'price': 3.0, 'end': '2019-02-04T05:10:00Z', 'id': 2, 'start': '2019-02-04T05:06:00Z', 'num_plates': 1, 'spice': 0, 'takeout_available': False}, headers={'X-CSRFToken': csrftoken})

class UserBehavior(TaskSet):
    tasks = {index: 4, search: 3, meal: 2, create_meal: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000