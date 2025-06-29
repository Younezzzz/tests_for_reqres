import requests



class UserAPi:
    def __init__(self, base_url, header):
        self.base_url = base_url
        self.header = header

    def  get_all_users(self, page):
        return requests.get(self.base_url+f"/users?page={page}",headers=self.header)

    def get_user_by_id(self,id):
        return requests.get(self.base_url+f"/users/{id}", headers=self.header)

    def new_user(self, payload: dict):
        return requests.post(self.base_url+"/users",json=payload, headers=self.header)

    def get_all_resources(self):
        return requests.get(self.base_url+"/unknown", headers=self.header)

    def get_resource_by_id(self,id):
        return requests.get(self.base_url+f"/unknown/{id}", headers=self.header)

    def update_user(self,id, name, job):
        payload = {"name": name, "job":job}
        return requests.put(self.base_url + f"/unknown/{id}", headers=self.header, json=payload)