import requests
from .settings import BASE_URL, API_TOKEN, REQUEST_TIMEOUT


class YougileClient:
    def __init__(self):
        self.base_url = BASE_URL.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"YOUGILE-KEY {API_TOKEN}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    # --- TASKS ---
    def create_task(self, payload: dict):
        """Создать задачу"""
        return self.session.post(f"{self.base_url}/tasks", json=payload, timeout=REQUEST_TIMEOUT)

    def get_task(self, task_id: str):
        """Получить задачу по ID"""
        return self.session.get(f"{self.base_url}/tasks/{task_id}", timeout=REQUEST_TIMEOUT)

    def update_task(self, task_id: str, payload: dict):
        """Изменить задачу"""
        return self.session.put(f"{self.base_url}/tasks/{task_id}", json=payload, timeout=REQUEST_TIMEOUT)
