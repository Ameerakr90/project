import requests

class PyBrowser:
    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, headers=None, params=None, data=None):
        response = self.session.request(method, url, headers=headers, params=params, data=data)
        return response

if __name__ == "__main__":
    browser = PyBrowser()
    response = browser.send_request("GET", "http://localhost:8000")
    print(response.status_code)
    print(response.text)
